---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-elementspecificat-a570922de8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/elementspecification/guide/ccvp_b_1261-element-specifications-guide/ccvp_m_1251-dialogflowparam-element.html
retrieved_at: 2026-08-21T17:24:45.486537+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

Updated: February 18, 2020

Chapter: DialogflowParam

## Chapter: DialogflowParam

# DialogflowParam

The DialogflowParam element can be used to engage the Google Dialogflow services. The DialogflowParam element is located under the Virtual Assistant–Voice group in the Call Studio Elements . This element is an extension of Form element and it engages the Speech Server resource on VVB to communicate with the Google Speech-to-Text Server to get user
                                    input and then send it to Dialogflow and fills param value from it. To indicate the Dialogflow server resource requirement,
                                    Call Studio creates a specific grammar - builtin:speech/transcribe - and sends it to VVB in VXML Page.

The DialogflowParam element works both with Cisco DTMF and Nuance ASR adaptors.

## Settings

Name (Label)

Type

Required

Single Setting Value

Substitution Allowed

Default

Notes

Input Mode

string

Yes

true

false

voice

The type of entry allowed for input. Possible values are voice (voice only) and dtmf+voice (DTMF and voice).

NoInput Timeout

int ≥ 0

Yes

true

true

5s

The maximum duration allowed for silence before a NoInput event is triggered. Possible values are standard time designations including non-negative numbers and a time unit. For example, 3s (for seconds) or 300 ms (for milliseconds).

Max NoInput Count

int ≥ 0

Yes

true

true

3

The maximum number of noinput events allowed during input capture. Possible values are int > 0 where 0 indicates infinite NoInput events permitted.

Max NoMatch Count

int ≥ 0

Yes

true

true

3

The maximum number of NoMatch events allowed during DTMF input capture. Possible values are int > 0 where 0 indicates infinite NoMatch events permitted.

DTMF Grammar

string

Yes

true

yes

None

This option is mandatory only if the input mode selected is DTMF and voice. It supports Cisco DTMF regex.

Send Digits to DF

boolean

Yes

true

true

true

This option is mandatory only if the input mode selected is DTMF and voice. It enables or disables submitting digits collected
                                       to the Dialogflow.

Secure Logging

boolean

Yes

true

true

false

Indicates whether logging of potentially sensitive data of the element is enabled. If this is set to true , the element's potentially sensitive data is not logged.

Termination Character

string

No

true

true

#

Terminates the voice stream or DTMF collection.

Max Input Time

int ≥ 0

Yes

true

true

30s

The maximum time (in seconds) the voice input is allowed to last. Possible values are positive integer values followed by
                                       s (seconds). For example, 50s . Default value is 30s .

Final Silence

int > 0

Yes

true

true

1s

The interval of silence (in seconds or milliseconds) that indicates the end of speech. Possible values are positive integer
                                       values followed by either s (seconds) or ms (milliseconds). For example, 3s and 3000ms . Default value is 1s .

intent

string

Yes

true

true

None

The current intent to be processed for parameter extraction.

variable

string

Yes

true

true

None

The variable to be processed for a particular intent mentioned in intent field.

Variable name should match the one defined in Google Dialogflow.

Last Parameter

boolean

Yes

true

true

false

This indicates end of parameter capture. If it is set to true , the intent is marked as complete.

Phrase Hints

string

No

true

true

None

This is comma separated string that lists the hints for recognition.

Hints are used to recognize a phrase or a word that is pronounced differently.

For example, Savings, Current.

Param Reset

boolean

Yes

true

true

false

If set to true, clears the parameter value captured from Dialogflow and enables reprompting.

## Custom VoiceXML Properties

Name (Label)

Type

Notes

Dialogflow.queryParams

.payload

JSON

Sets the payload to be sent to Dialogflow.

Dialogflow.queryParams

.timeZone

String

Sets the timezone to be sent to Dialogflow.

For example, America/New_York, Europe/Paris.

Dialogflow.queryParams.geoLocation

String

(comma separated value)

Sets the geographical location to be sent to Dialogflow.

For example, "50.0,50.0".

Dialogflow.queryParams.

sessionEntityTypes

JSON

Sets the additional entity types to be sent to Dialogflow.

For example, [{'name': 'class','entityOverrideMode': 'ENTITY_OVERRIDE_MODE_OVERRIDE','entities': [{'value': 'economy','synonyms': ['eco',
                                          'economy']}]}] .

Dialogflow.queryParams

.sentimentAnalysisRequestConfig

Boolean

Configures the type of sentiment analysis to perform. If not provided, sentiment analysis is not performed.

Sentiment Analysis is currently available only for Enterprise Edition agents.

## Element Data

The following table lists the data that is stored in element after processing the DialogflowParam element.

Element Data

Description

action

This is the action parameter from Dialogflow.

fulillment_text

This is fulfillment text from Dialogflow.

input_type

Indicates the type of input captured ( dtmf or dtmf+voice ).

intent

Indicates the intent of a parameter.

json

Contains JSON response from Dialogflow.

For response formats, see json details in the Dialogflow Element Data .

asr_json

Contains JSON response from Speech Recognition.

original_value

Indicates the parameter value as uttered by the user in string.

value

This is the parameter value returned by Dialogflow if input type is voice .

If input type is dtmf , it contains the DTMF key that is pressed by the user.

confidence

The Speech recognition confidence between 0.0 and 1.0. A higher number indicates a greater probability that the recognized
                                       words are correct. The default of 0.0 is a sentinel value indicating that confidence was not set.

sentiment_score

Sentiment score of the user input.

## Exit States

Exit State

Description

Done

This is returned when the configured parameter is filled.

Intent_Change

This is returned when Dialogflow switches to a different intent whose filling slot is based on user utterance.

MAX_NoInput

This state is encountered when there is no input from the user for a specified duration as configured in the setting.

MAX_NoMatch

This state is returned when the variable or parameter mentioned in element setting is not matched for specified number of
                                       times as mentioned in settings.

If the input type is dtmf+voice , this state is encountered when the DTMF input does not match regex grammar for the specified number of times as mentioned
                                       in settings.

## Audio Group

### Form Data Capture

Name (Label)

Required

Max1

Notes

initial_audio_group (Initial)

Yes

Yes

Played when the voice element begins.

nomatch_audio_group (NoMatch)

No

No

Played when a NoMatch event occurs.

This is applicable only when the input type is dtmf+voice .

noinput_audio_group (NoInput)

No

No

Played when a NoInput event occurs.

### End

Name (Label)

Required

Max1

Notes

done_audio_group (Done)

No

Yes

Played when the form data capture is completed and the voice element exits with the Done exit state.

## Folder and Class Information

Studio Element Folder Name

Class Name

Form

com.audium.server.voiceElement.form

## Events

Name (Label)

Notes

Event Type

You can select Java Exception , VXML Event , or Hotlink as the event handler for this element.

| The DialogflowParam element can be used to engage the Google Dialogflow services. The DialogflowParam element is located under the Virtual Assistant–Voice group in the Call Studio Elements . This element is an extension of Form element and it engages the Speech Server resource on VVB to communicate with the Google Speech-to-Text Server to get user
                                    input and then send it to Dialogflow and fills param value from it. To indicate the Dialogflow server resource requirement,
                                    Call Studio creates a specific grammar - builtin:speech/transcribe - and sends it to VVB in VXML Page. Note The DialogflowParam element works both with Cisco DTMF and Nuance ASR adaptors. | Note | The DialogflowParam element works both with Cisco DTMF and Nuance ASR adaptors. |
|---|---|---|
| Note | The DialogflowParam element works both with Cisco DTMF and Nuance ASR adaptors. |

| Note | The DialogflowParam element works both with Cisco DTMF and Nuance ASR adaptors. |
|---|---|

| Name (Label) | Type | Required | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Input Mode | string | Yes | true | false | voice | The type of entry allowed for input. Possible values are voice (voice only) and dtmf+voice (DTMF and voice). |
| NoInput Timeout | int ≥ 0 | Yes | true | true | 5s | The maximum duration allowed for silence before a NoInput event is triggered. Possible values are standard time designations including non-negative numbers and a time unit. For example, 3s (for seconds) or 300 ms (for milliseconds). |
| Max NoInput Count | int ≥ 0 | Yes | true | true | 3 | The maximum number of noinput events allowed during input capture. Possible values are int > 0 where 0 indicates infinite NoInput events permitted. |
| Max NoMatch Count | int ≥ 0 | Yes | true | true | 3 | The maximum number of NoMatch events allowed during DTMF input capture. Possible values are int > 0 where 0 indicates infinite NoMatch events permitted. |
| DTMF Grammar | string | Yes | true | yes | None | This option is mandatory only if the input mode selected is DTMF and voice. It supports Cisco DTMF regex. |
| Send Digits to DF | boolean | Yes | true | true | true | This option is mandatory only if the input mode selected is DTMF and voice. It enables or disables submitting digits collected
                                       to the Dialogflow. |
| Secure Logging | boolean | Yes | true | true | false | Indicates whether logging of potentially sensitive data of the element is enabled. If this is set to true , the element's potentially sensitive data is not logged. |
| Termination Character | string | No | true | true | # | Terminates the voice stream or DTMF collection. |
| Max Input Time | int ≥ 0 | Yes | true | true | 30s | The maximum time (in seconds) the voice input is allowed to last. Possible values are positive integer values followed by
                                       s (seconds). For example, 50s . Default value is 30s . |
| Final Silence | int > 0 | Yes | true | true | 1s | The interval of silence (in seconds or milliseconds) that indicates the end of speech. Possible values are positive integer
                                       values followed by either s (seconds) or ms (milliseconds). For example, 3s and 3000ms . Default value is 1s . |
| intent | string | Yes | true | true | None | The current intent to be processed for parameter extraction. |
| variable | string | Yes | true | true | None | The variable to be processed for a particular intent mentioned in intent field. Note Variable name should match the one defined in Google Dialogflow. | Note | Variable name should match the one defined in Google Dialogflow. |
| Note | Variable name should match the one defined in Google Dialogflow. |
| Last Parameter | boolean | Yes | true | true | false | This indicates end of parameter capture. If it is set to true , the intent is marked as complete. |
| Phrase Hints | string | No | true | true | None | This is comma separated string that lists the hints for recognition. Hints are used to recognize a phrase or a word that is pronounced differently. For example, Savings, Current. |
| Param Reset | boolean | Yes | true | true | false | If set to true, clears the parameter value captured from Dialogflow and enables reprompting. |

| Note | Variable name should match the one defined in Google Dialogflow. |
|---|---|

| Name (Label) | Type | Notes |
|---|---|---|
| Dialogflow.queryParams .payload | JSON | Sets the payload to be sent to Dialogflow. |
| Dialogflow.queryParams .timeZone | String | Sets the timezone to be sent to Dialogflow. For example, America/New_York, Europe/Paris. |
| Dialogflow.queryParams.geoLocation | String (comma separated value) | Sets the geographical location to be sent to Dialogflow. For example, "50.0,50.0". |
| Dialogflow.queryParams. sessionEntityTypes | JSON | Sets the additional entity types to be sent to Dialogflow. For example, [{'name': 'class','entityOverrideMode': 'ENTITY_OVERRIDE_MODE_OVERRIDE','entities': [{'value': 'economy','synonyms': ['eco',
                                          'economy']}]}] . |
| Dialogflow.queryParams .sentimentAnalysisRequestConfig | Boolean | Configures the type of sentiment analysis to perform. If not provided, sentiment analysis is not performed. Note Sentiment Analysis is currently available only for Enterprise Edition agents. | Note | Sentiment Analysis is currently available only for Enterprise Edition agents. |
| Note | Sentiment Analysis is currently available only for Enterprise Edition agents. |

| Note | Sentiment Analysis is currently available only for Enterprise Edition agents. |
|---|---|

| Element Data | Description |
|---|---|
| action | This is the action parameter from Dialogflow. |
| fulillment_text | This is fulfillment text from Dialogflow. |
| input_type | Indicates the type of input captured ( dtmf or dtmf+voice ). |
| intent | Indicates the intent of a parameter. |
| json | Contains JSON response from Dialogflow. For response formats, see json details in the Dialogflow Element Data . |
| asr_json | Contains JSON response from Speech Recognition. |
| original_value | Indicates the parameter value as uttered by the user in string. |
| value | This is the parameter value returned by Dialogflow if input type is voice . If input type is dtmf , it contains the DTMF key that is pressed by the user. |
| confidence | The Speech recognition confidence between 0.0 and 1.0. A higher number indicates a greater probability that the recognized
                                       words are correct. The default of 0.0 is a sentinel value indicating that confidence was not set. |
| sentiment_score | Sentiment score of the user input. |

| Exit State | Description |
|---|---|
| Done | This is returned when the configured parameter is filled. |
| Intent_Change | This is returned when Dialogflow switches to a different intent whose filling slot is based on user utterance. |
| MAX_NoInput | This state is encountered when there is no input from the user for a specified duration as configured in the setting. |
| MAX_NoMatch | This state is returned when the variable or parameter mentioned in element setting is not matched for specified number of
                                       times as mentioned in settings. If the input type is dtmf+voice , this state is encountered when the DTMF input does not match regex grammar for the specified number of times as mentioned
                                       in settings. |

| Name (Label) | Required | Max1 | Notes |
|---|---|---|---|
| initial_audio_group (Initial) | Yes | Yes | Played when the voice element begins. |
| nomatch_audio_group (NoMatch) | No | No | Played when a NoMatch event occurs. This is applicable only when the input type is dtmf+voice . |
| noinput_audio_group (NoInput) | No | No | Played when a NoInput event occurs. |

| Name (Label) | Required | Max1 | Notes |
|---|---|---|---|
| done_audio_group (Done) | No | Yes | Played when the form data capture is completed and the voice element exits with the Done exit state. |

| Studio Element Folder Name | Class Name |
|---|---|
| Form | com.audium.server.voiceElement.form |

| Name (Label) | Notes |
|---|---|
| Event Type | You can select Java Exception , VXML Event , or Hotlink as the event handler for this element. |