---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-elementspecificat-bdd822e639
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/elementspecification/guide/ccvp_b_1261-element-specifications-guide/ccvp_m_1251-dialogflowintent-element.html
retrieved_at: 2026-08-21T17:24:40.924002+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

Updated: February 18, 2020

Chapter: DialogflowIntent

## Chapter: DialogflowIntent

# DialogflowIntent

The DialogflowIntent element is used to engage the Google Dialogflow services. The DialogflowIntent element is located under the Virtual Assistant–Voice group in the Call Studio Elements . This element is an extension of the Form element and it engages the Speech Server resource on VVB to communicate with the Google Speech to Text Server to get user
                                    input and then send it to Dialogflow and finds user intent from it.. To indicate the Dialogflow server resource requirement,
                                    Call Studio creates a specific grammar - builtin:speech/transcribe - and sends it to VVB in VXML Page.

The DialogflowIntent element works both with Cisco DTMF and Nuance ASR adaptors.

Use dtmf+voice as the input type only if you do not have any DialogflowParam associated with this element.

## Settings

Name (Label)

Type

Required

Single Setting Value

Substitution Allowed

Default

Notes

Service Account ID

string

No

true

true

None

Dialogflow project ID that is configured for your intents and NLP modelling.

Copy the corresponding project Json key file to %CVP_HOME%\conf . Naming convention of the key file must be <Service Account ID>.json .

See the Virtual Assistant–Voice > VAV Onboarding for Non-OEM Users > Prerequisites section in the Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html for the procedure to generate the key file for Dialogflow.

Input Mode

string

Yes

true

false

voice

The type of entry allowed for input. Possible values are voice (only voice input) and dtmf+voice (DTMF and voice input).

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

yes

yes

None

This option is mandatory only if the input type selected is dtmf+voice . It supports Cisco DTMF regex.

Secure Logging

boolean

Yes

true

true

false

Indicates whether logging of potentially sensitive data of the element is enabled. If this is set to true , the element's potentially sensitive data is not logged.

Termination Character

String

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

Recognize.

phraseHints

String

No

true

true

None

This is comma separated string that lists the hints for recognition.

Hints are used to recognize a phrase or a word that is pronounced differently.

For example, Savings, Current.

Recognize.

alternateLanguages

String

No

true

true

None

Comma separated string of up to 3 additional BCP-47 language tags, listing possible alternative languages of the supplied
                                       audio other than the default language.

## Custom VoiceXML Properties

Name (Label)

Type

Notes

Dialogflow.regionId

String

Sets the region to be sent to Dialogflow.

This property should be configured in the root document of the project.

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

Dialogflow.queryParams

.sentimentAnalysisRequestConfig

Boolean

Configures the type of sentiment analysis to perform. If not provided, sentiment analysis is not performed.

Sentiment Analysis is currently available only for Enterprise Edition agents.

Dialogflow.profileId

String

Conversation profile is used to configure agents and connected services for the conversation on the Google Dialogflow Project.

Create a profile for your CCAI-allowed project by following these steps . (Link will require listing on Google CCAI Documentation allowed list ).

CCAI.configId

String

Config ID to fetch Dialogflow Json key from WebexCC Tenant Management. If Config ID is not provided, it tries to fetch the
                                       key from local file system, using the Service Account ID field mentioned in element settings.

If Config ID and Service Account ID are not provided, default config will be fetched from the Webex CC Tenant Hub.

Json key fetched from Webex CC is cached and flushed after 60 minutes. Any change in WebEX CC Tenant Management takes one
                                       hour to reflect in CVP. To reflect immediately, restart the VXML server.

Default flush time can be changed using the following IVR property in the <CVP_HOME>/conf/ivr.properties file:

IVR.CcaiConfigFlushTimeoutInMinutes=60

## Element Data

The following table lists the data that is stored in element after processing the DialogflowIntent element.

Element Data

Description

action

This is the action parameter from Dialogflow.

fulillment_text

This is the fulfillment text from Dialogflow.

input_type

Indicates the type of input captured ( dtmf or dtmf+voice ).

json

Contains JSON response from Dialogflow.

For response formats, see json details in the Dialogflow Element Data .

asr_json

Contains JSON response from Speech Recognition.

original_value

This is the text that is transcribed from voice.

This is applicable only if the input type is voice .

value

This is the name of the intent that is matched by the element if input type is voice .

If input type is dtmf , it contains the DTMF key that is pressed by the user.

confidence

The Speech recognition confidence between 0.0 and 1.0. A higher number indicates a greater probability that the recognized
                                       words are correct. The default of 0.0 is a sentinel value indicating that confidence was not set.

language_code

The language code that was triggered during recognition.

Also see Recognize.alternateLanguages under Settings .

sentiment_score

Sentiment score of the user input.

## Exit States

Exit State

Description

Done

This is returned after matching the intent. For DTMF, this state is returned when the DTMF input matches DTMF regex grammar.

MAX_NOINPUT

This state is encountered when there is no input from the user for a specified duration as configured in the setting.

MAX_NoMatch

This state is never retuned if the input type is voice.

If the input type is dtmf and voice , this state is encountered when the DTMF input does not match regex grammar for the specified number of times as mentioned
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

This is applicable only when the input mode is DTMF and voice.

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

| The DialogflowIntent element is used to engage the Google Dialogflow services. The DialogflowIntent element is located under the Virtual Assistant–Voice group in the Call Studio Elements . This element is an extension of the Form element and it engages the Speech Server resource on VVB to communicate with the Google Speech to Text Server to get user
                                    input and then send it to Dialogflow and finds user intent from it.. To indicate the Dialogflow server resource requirement,
                                    Call Studio creates a specific grammar - builtin:speech/transcribe - and sends it to VVB in VXML Page. Note The DialogflowIntent element works both with Cisco DTMF and Nuance ASR adaptors. Use dtmf+voice as the input type only if you do not have any DialogflowParam associated with this element. | Note | The DialogflowIntent element works both with Cisco DTMF and Nuance ASR adaptors. Use dtmf+voice as the input type only if you do not have any DialogflowParam associated with this element. |
|---|---|---|
| Note | The DialogflowIntent element works both with Cisco DTMF and Nuance ASR adaptors. Use dtmf+voice as the input type only if you do not have any DialogflowParam associated with this element. |

| Note | The DialogflowIntent element works both with Cisco DTMF and Nuance ASR adaptors. Use dtmf+voice as the input type only if you do not have any DialogflowParam associated with this element. |
|---|---|

| Name (Label) | Type | Required | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Service Account ID | string | No | true | true | None | Dialogflow project ID that is configured for your intents and NLP modelling. Copy the corresponding project Json key file to %CVP_HOME%\conf . Naming convention of the key file must be <Service Account ID>.json . See the Virtual Assistant–Voice > VAV Onboarding for Non-OEM Users > Prerequisites section in the Cisco Unified Contact Center Enterprise Features Guide at https://www.cisco.com/c/en/us/support/customer-collaboration/unified-contact-center-enterprise/products-feature-guides-list.html for the procedure to generate the key file for Dialogflow. |
| Input Mode | string | Yes | true | false | voice | The type of entry allowed for input. Possible values are voice (only voice input) and dtmf+voice (DTMF and voice input). |
| NoInput Timeout | int ≥ 0 | Yes | true | true | 5s | The maximum duration allowed for silence before a NoInput event is triggered. Possible values are standard time designations including non-negative numbers and a time unit. For example, 3s (for seconds) or 300 ms (for milliseconds). |
| Max NoInput Count | int ≥ 0 | Yes | true | true | 3 | The maximum number of noinput events allowed during input capture. Possible values are int > 0 where 0 indicates infinite NoInput events permitted. |
| Max NoMatch Count | int ≥ 0 | Yes | true | true | 3 | The maximum number of NoMatch events allowed during DTMF input capture. Possible values are int > 0 where 0 indicates infinite NoMatch events permitted. |
| DTMF Grammar | string | Yes | yes | yes | None | This option is mandatory only if the input type selected is dtmf+voice . It supports Cisco DTMF regex. |
| Secure Logging | boolean | Yes | true | true | false | Indicates whether logging of potentially sensitive data of the element is enabled. If this is set to true , the element's potentially sensitive data is not logged. |
| Termination Character | String | No | true | true | # | Terminates the voice stream or DTMF collection. |
| Max Input Time | int ≥ 0 | Yes | true | true | 30s | The maximum time (in seconds) the voice input is allowed to last. Possible values are positive integer values followed by
                                       s (seconds). For example, 50s . Default value is 30s . |
| Final Silence | int > 0 | Yes | true | true | 1s | The interval of silence (in seconds or milliseconds) that indicates the end of speech. Possible values are positive integer
                                       values followed by either s (seconds) or ms (milliseconds). For example, 3s and 3000ms . Default value is 1s . |
| Recognize. phraseHints | String | No | true | true | None | This is comma separated string that lists the hints for recognition. Hints are used to recognize a phrase or a word that is pronounced differently. For example, Savings, Current. |
| Recognize. alternateLanguages | String | No | true | true | None | Comma separated string of up to 3 additional BCP-47 language tags, listing possible alternative languages of the supplied
                                       audio other than the default language. |

| Name (Label) | Type | Notes |
|---|---|---|
| Dialogflow.regionId | String | Sets the region to be sent to Dialogflow. This property should be configured in the root document of the project. |
| Dialogflow.queryParams .payload | JSON | Sets the payload to be sent to Dialogflow. |
| Dialogflow.queryParams .timeZone | String | Sets the timezone to be sent to Dialogflow. For example, America/New_York, Europe/Paris. |
| Dialogflow.queryParams.geoLocation | String (comma separated value) | Sets the geographical location to be sent to Dialogflow. For example, "50.0,50.0". |
| Dialogflow.queryParams .sentimentAnalysisRequestConfig | Boolean | Configures the type of sentiment analysis to perform. If not provided, sentiment analysis is not performed. Note Sentiment Analysis is currently available only for Enterprise Edition agents. | Note | Sentiment Analysis is currently available only for Enterprise Edition agents. |
| Note | Sentiment Analysis is currently available only for Enterprise Edition agents. |
| Dialogflow.profileId | String | Conversation profile is used to configure agents and connected services for the conversation on the Google Dialogflow Project. Create a profile for your CCAI-allowed project by following these steps . (Link will require listing on Google CCAI Documentation allowed list ). |
| CCAI.configId | String | Config ID to fetch Dialogflow Json key from WebexCC Tenant Management. If Config ID is not provided, it tries to fetch the
                                       key from local file system, using the Service Account ID field mentioned in element settings. If Config ID and Service Account ID are not provided, default config will be fetched from the Webex CC Tenant Hub. Json key fetched from Webex CC is cached and flushed after 60 minutes. Any change in WebEX CC Tenant Management takes one
                                       hour to reflect in CVP. To reflect immediately, restart the VXML server. Default flush time can be changed using the following IVR property in the <CVP_HOME>/conf/ivr.properties file: IVR.CcaiConfigFlushTimeoutInMinutes=60 |

| Note | Sentiment Analysis is currently available only for Enterprise Edition agents. |
|---|---|

| Element Data | Description |
|---|---|
| action | This is the action parameter from Dialogflow. |
| fulillment_text | This is the fulfillment text from Dialogflow. |
| input_type | Indicates the type of input captured ( dtmf or dtmf+voice ). |
| json | Contains JSON response from Dialogflow. For response formats, see json details in the Dialogflow Element Data . |
| asr_json | Contains JSON response from Speech Recognition. |
| original_value | This is the text that is transcribed from voice. This is applicable only if the input type is voice . |
| value | This is the name of the intent that is matched by the element if input type is voice . If input type is dtmf , it contains the DTMF key that is pressed by the user. |
| confidence | The Speech recognition confidence between 0.0 and 1.0. A higher number indicates a greater probability that the recognized
                                       words are correct. The default of 0.0 is a sentinel value indicating that confidence was not set. |
| language_code | The language code that was triggered during recognition. Also see Recognize.alternateLanguages under Settings . |
| sentiment_score | Sentiment score of the user input. |

| Exit State | Description |
|---|---|
| Done | This is returned after matching the intent. For DTMF, this state is returned when the DTMF input matches DTMF regex grammar. |
| MAX_NOINPUT | This state is encountered when there is no input from the user for a specified duration as configured in the setting. |
| MAX_NoMatch | This state is never retuned if the input type is voice. If the input type is dtmf and voice , this state is encountered when the DTMF input does not match regex grammar for the specified number of times as mentioned
                                       in settings. |

| Name (Label) | Required | Max1 | Notes |
|---|---|---|---|
| initial_audio_group (Initial) | Yes | Yes | Played when the voice element begins. |
| nomatch_audio_group (NoMatch) | No | No | Played when a NoMatch event occurs. This is applicable only when the input mode is DTMF and voice. |
| noinput_audio_group (NoInput) | No | No | Played when a NoInput event occurs. |

| Name (Label) | Required | Max1 | Notes |
|---|---|---|---|
| done_audio_group (Done) | No | Yes | Played when the form data capture is completed and the voice element exits with the Done exit state. |