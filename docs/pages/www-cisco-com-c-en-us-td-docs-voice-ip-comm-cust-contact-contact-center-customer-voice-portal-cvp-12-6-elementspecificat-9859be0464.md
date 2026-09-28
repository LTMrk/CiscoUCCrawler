---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-elementspecificat-9859be0464
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/elementspecification/guide/ccvp_b_1261-element-specifications-guide/ccvp_m_1251-dialogflow-element.html
retrieved_at: 2026-08-21T17:24:36.688737+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

Updated: February 18, 2020

Chapter: Dialogflow

## Chapter: Dialogflow

# Dialogflow

The Dialogflow element can be used to engage the Google Dialogflow services. The Dialogflow element is located under the Virtual Assistant–Voice group in the Call Studio Elements . This element is an extension of Form element and it engages the special resource on VVB called Speech Server to communicate with the Dialogflow Server. To indicate
                                    the Dialogflow server resource requirement, Call Studio creates a specific grammar - builtin:speech/nlp@dialogflow - and sends it to VVB in VXML Page.

The Dialogflow element works both with Cisco DTMF and Nuance ASR adaptors.

The Dialogflow element supports both speech and DTMF inputs. # is the default DTMF termchar for terminating the input.

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

Input Mode

string

Yes

true

false

voice

The type of entry allowed for input. Possible values are voice (only voice input) and dtmf+voice (DTMF and voice input).

Audio Output

boolean

Yes

true

false

false

Whether to use the Dialogflow feature to get the audio output from Dialogflow. Can be used while performing Slot / Intent
                                       fulfilment at Dialogflow.

NoInput Timeout

int ≥ 0

Yes

true

true

5s

The maximum duration allowed for silence before a NoInput event is triggered. Possible values are standard time designations including both non-negative numbers and a time unit.

For example, 3s for seconds or 300 ms for milliseconds.

Max NoInput Count

int ≥ 0

Yes

true

true

3

The maximum number of noinput events allowed during input capture. Possible values int > 0 where 0 indicates infinite NoInput events allowed.

Secure Logging

boolean

Yes

true

true

false

Indicates whether logging of potentially sensitive data of the element is enabled. If set to true , the element's potentially sensitive data is not logged.

Terminiation Character

Terminate the voice stream or DTMF collection.

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

Initiation Text

string

No

true

true

Hello

Text sent to initiate the dialog with Dialogflow. The response for this is the welcome intent from Dialogflow.

This is applicable only when Audio Output is set to true .

## Custom VoiceXML Properties

Name (Label)

Type

Notes

Dialogflow.regionId

String

Sets the region to be sent to Dialogflow.

This property should be configured in the root document of the project.

Region ID is picked from the conversation profile ID if Cloud Connect is configured and config ID is available; else Region
                                       ID is picked from the VXML properties.

Dialogflow.queryParams

.payload

JSON

Sets the payload to be sent to Dialogflow.

Dialogflow.queryParams

.timeZone

String

Sets the timezone to be sent to Dialogflow.

For example, America/New_York, Europe/Paris.

Dialogflow.queryParams.

geoLocation

String

Sets the geographical location to be sent to Dialogflow.

For example, "50.0,50.0".

Dialogflow.queryParams

.sessionEntityTypes

JSON

Sets the additional entity types to be sent to Dialogflow.

For example, [{name:class,entityOverrideMode:ENTITY_OVERRIDE_MODE_OVERRIDE,entities:[{value:economy,synonyms:[eco,economy]}]}] .

Dialogflow.queryParams

.sentimentAnalysisRequestConfig

Boolean

Configures the type of sentiment analysis to perform. If not provided, sentiment analysis is not performed.

Sentiment Analysis is currently available only for Enterprise Edition agents.

Recognize.singleUtterance

Boolean

Indicates whether this request should automatically end after speech is no longer detected. If this parameter is enabled,
                                       cloud speech-to-text will detect pauses, silence, or non-speech audio to determine when to end recognition. If this parameter
                                       is disabled, the stream will continue to listen and process audio until either the stream is closed directly, or the stream's
                                       length limit is reached.

The default setting for this parameter is true .

Recognize.model

String

This is used to specify the machine learning model to be used by the cloud speech-to-text transcription to improve the recognition
                                       results.

For example, see https://cloud.google.com/speech-to-text/docs/basics

Dialogflow.profileId

String

Conversation profile is used to configure agents and connected services for the conversation on the Google Dialogflow Project.

Create a profile for your CCAI-allowed project by following these steps . (Link will require listing on Google CCAI Documentation allowed list ).

CCAI.configId

String

Config ID to fetch Dialogflow Json key from WebexCC Tenant Management. If Config ID is not provided, it tries to fetch the
                                       key from local file system, using the Service Account ID field mentioned in element settings.

If Config ID and Service Account ID are not provided, default config will be fetched from the Webex CC Tenant Hub.

Json key fetched from WebExCC is cached and flushed after 60 minutes. Any change in Webex CC Tenant Management takes one hour
                                       to reflect in CVP. To reflect immediately, restart the speech server.

Default flush time can be changed using the following speech server property in the <SPEECHSERVER_HOME>/conf/speechserver.properties file:

com.cisco.cloudconnect.configFlushTimeoutInMinutes=60

## Element Data

Element Data

Notes

intent

Intent identified.

query_text

User input.

fulfilment_text

Fulfilment text returned by Dialogflow.

value

JSON value returned by Dialogflow.

action

Returns the action associated with the intent.

is_complete

Indicates whether all the required parameters are filled. This can be used to derive exit states with decision element.

If all parameters are not filled, it is false .

If an intent has no parameters, this is always true .

json

Contains JSON response from Dialogflow.

Response formats:

From Google CCAI: "detectIntentResponse": {"queryResult": {}}

From Google DialogFlow: "queryResult": {}

Refer to Google Documentation for detailed response structure of AutomatedAgentReply and StreamingDetectIntentResponse .

confidence

The Speech recognition confidence between 0.0 and 1.0. A higher number indicates a greater probability that the recognized
                                       words are correct. The default of 0.0 is a sentinel value indicating that confidence was not set.

language_code

The language code that was triggered during recognition.

sentiment_score

Sentiment score of the user input.

## Exit States

Name

Notes

done

This state is returned after receiving response from Dialogflow. This indicates that the processing from Dialogflow has been
                                       completed.

max_noinput

Maximum number of noinput events that have occurred. If noinput max count is 0 , this exit state will not occur.

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

com.audium.server.voiceElement.form .

## Events

Name (Label)

Class Name

Event Type

You can select Java Exception , VXML Event , or Hotlink as event handler for this element.

| The Dialogflow element can be used to engage the Google Dialogflow services. The Dialogflow element is located under the Virtual Assistant–Voice group in the Call Studio Elements . This element is an extension of Form element and it engages the special resource on VVB called Speech Server to communicate with the Dialogflow Server. To indicate
                                    the Dialogflow server resource requirement, Call Studio creates a specific grammar - builtin:speech/nlp@dialogflow - and sends it to VVB in VXML Page. Note The Dialogflow element works both with Cisco DTMF and Nuance ASR adaptors. The Dialogflow element supports both speech and DTMF inputs. # is the default DTMF termchar for terminating the input. | Note | The Dialogflow element works both with Cisco DTMF and Nuance ASR adaptors. The Dialogflow element supports both speech and DTMF inputs. # is the default DTMF termchar for terminating the input. |
|---|---|---|
| Note | The Dialogflow element works both with Cisco DTMF and Nuance ASR adaptors. The Dialogflow element supports both speech and DTMF inputs. # is the default DTMF termchar for terminating the input. |

| Note | The Dialogflow element works both with Cisco DTMF and Nuance ASR adaptors. The Dialogflow element supports both speech and DTMF inputs. # is the default DTMF termchar for terminating the input. |
|---|---|

| Name (Label) | Type | Required | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Service Account ID | string | No | true | true | None | Dialogflow project ID that is configured for your intents and NLP modelling. |
| Input Mode | string | Yes | true | false | voice | The type of entry allowed for input. Possible values are voice (only voice input) and dtmf+voice (DTMF and voice input). |
| Audio Output | boolean | Yes | true | false | false | Whether to use the Dialogflow feature to get the audio output from Dialogflow. Can be used while performing Slot / Intent
                                       fulfilment at Dialogflow. |
| NoInput Timeout | int ≥ 0 | Yes | true | true | 5s | The maximum duration allowed for silence before a NoInput event is triggered. Possible values are standard time designations including both non-negative numbers and a time unit. For example, 3s for seconds or 300 ms for milliseconds. |
| Max NoInput Count | int ≥ 0 | Yes | true | true | 3 | The maximum number of noinput events allowed during input capture. Possible values int > 0 where 0 indicates infinite NoInput events allowed. |
| Secure Logging | boolean | Yes | true | true | false | Indicates whether logging of potentially sensitive data of the element is enabled. If set to true , the element's potentially sensitive data is not logged. |
| Terminiation Character | string | No | true | true | # | Terminate the voice stream or DTMF collection. |
| Max Input Time | int ≥ 0 | Yes | true | true | 30s | The maximum time (in seconds) the voice input is allowed to last. Possible values are positive integer values followed by
                                       s (seconds). For example, 50s . Default value is 30s . |
| Final Silence | int > 0 | Yes | true | true | 1s | The interval of silence (in seconds or milliseconds) that indicates the end of speech. Possible values are positive integer
                                       values followed by either s (seconds) or ms (milliseconds). For example, 3s and 3000ms . Default value is 1s . |
| Initiation Text | string | No | true | true | Hello | Text sent to initiate the dialog with Dialogflow. The response for this is the welcome intent from Dialogflow. This is applicable only when Audio Output is set to true . |

| Name (Label) | Type | Notes |
|---|---|---|
| Dialogflow.regionId | String | Sets the region to be sent to Dialogflow. This property should be configured in the root document of the project. Region ID is picked from the conversation profile ID if Cloud Connect is configured and config ID is available; else Region
                                       ID is picked from the VXML properties. |
| Dialogflow.queryParams .payload | JSON | Sets the payload to be sent to Dialogflow. |
| Dialogflow.queryParams .timeZone | String | Sets the timezone to be sent to Dialogflow. For example, America/New_York, Europe/Paris. |
| Dialogflow.queryParams. geoLocation | String | Sets the geographical location to be sent to Dialogflow. For example, "50.0,50.0". |
| Dialogflow.queryParams .sessionEntityTypes | JSON | Sets the additional entity types to be sent to Dialogflow. For example, [{name:class,entityOverrideMode:ENTITY_OVERRIDE_MODE_OVERRIDE,entities:[{value:economy,synonyms:[eco,economy]}]}] . |
| Dialogflow.queryParams .sentimentAnalysisRequestConfig | Boolean | Configures the type of sentiment analysis to perform. If not provided, sentiment analysis is not performed. Note Sentiment Analysis is currently available only for Enterprise Edition agents. | Note | Sentiment Analysis is currently available only for Enterprise Edition agents. |
| Note | Sentiment Analysis is currently available only for Enterprise Edition agents. |
| Recognize.singleUtterance | Boolean | Indicates whether this request should automatically end after speech is no longer detected. If this parameter is enabled,
                                       cloud speech-to-text will detect pauses, silence, or non-speech audio to determine when to end recognition. If this parameter
                                       is disabled, the stream will continue to listen and process audio until either the stream is closed directly, or the stream's
                                       length limit is reached. The default setting for this parameter is true . |
| Recognize.model | String | This is used to specify the machine learning model to be used by the cloud speech-to-text transcription to improve the recognition
                                       results. For example, see https://cloud.google.com/speech-to-text/docs/basics |
| Dialogflow.profileId | String | Conversation profile is used to configure agents and connected services for the conversation on the Google Dialogflow Project. Create a profile for your CCAI-allowed project by following these steps . (Link will require listing on Google CCAI Documentation allowed list ). |
| CCAI.configId | String | Config ID to fetch Dialogflow Json key from WebexCC Tenant Management. If Config ID is not provided, it tries to fetch the
                                       key from local file system, using the Service Account ID field mentioned in element settings. If Config ID and Service Account ID are not provided, default config will be fetched from the Webex CC Tenant Hub. Json key fetched from WebExCC is cached and flushed after 60 minutes. Any change in Webex CC Tenant Management takes one hour
                                       to reflect in CVP. To reflect immediately, restart the speech server. Default flush time can be changed using the following speech server property in the <SPEECHSERVER_HOME>/conf/speechserver.properties file: com.cisco.cloudconnect.configFlushTimeoutInMinutes=60 |

| Note | Sentiment Analysis is currently available only for Enterprise Edition agents. |
|---|---|

| Element Data | Notes |
|---|---|
| intent | Intent identified. |
| query_text | User input. |
| fulfilment_text | Fulfilment text returned by Dialogflow. |
| value | JSON value returned by Dialogflow. |
| action | Returns the action associated with the intent. |
| is_complete | Indicates whether all the required parameters are filled. This can be used to derive exit states with decision element. If all parameters are not filled, it is false . If an intent has no parameters, this is always true . |
| json | Contains JSON response from Dialogflow. Response formats: From Google CCAI: "detectIntentResponse": {"queryResult": {}} From Google DialogFlow: "queryResult": {} Refer to Google Documentation for detailed response structure of AutomatedAgentReply and StreamingDetectIntentResponse . |
| confidence | The Speech recognition confidence between 0.0 and 1.0. A higher number indicates a greater probability that the recognized
                                       words are correct. The default of 0.0 is a sentinel value indicating that confidence was not set. |
| language_code | The language code that was triggered during recognition. |
| sentiment_score | Sentiment score of the user input. |

| Name | Notes |
|---|---|
| done | This state is returned after receiving response from Dialogflow. This indicates that the processing from Dialogflow has been
                                       completed. |
| max_noinput | Maximum number of noinput events that have occurred. If noinput max count is 0 , this exit state will not occur. |

| Name (Label) | Required | Max1 | Notes |
|---|---|---|---|
| initial_audio_group (Initial) | Yes | Yes | Played when the voice element begins. |
| noinput_audio_group (NoInput) | No | No | Played when a NoInput event occurs. |

| Name (Label) | Required | Max1 | Notes |
|---|---|---|---|
| done_audio_group (Done) | No | Yes | Played when the form data capture is completed and the voice element exits with the Done exit state. |

| Studio Element Folder Name | Class Name |
|---|---|
| Form | com.audium.server.voiceElement.form . |

| Name (Label) | Class Name |
|---|---|
| Event Type | You can select Java Exception , VXML Event , or Hotlink as event handler for this element. |