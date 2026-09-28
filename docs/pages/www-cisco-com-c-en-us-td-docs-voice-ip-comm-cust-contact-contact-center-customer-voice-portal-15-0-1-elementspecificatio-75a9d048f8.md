---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-elementspecificatio-75a9d048f8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/elementspecification/guide/ccvp_b_150-element-specifications-guide-for-cvp-vxml-and-call-studio/dialogflowCX.html
retrieved_at: 2026-08-21T17:11:04.407142+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

Updated: April 30, 2025

Chapter: DialogflowCX

## Chapter: DialogflowCX

# DialogflowCX

The DialogflowCX element can be used to engage the Google Dialogflow CX services. The DialogflowCX element is located under the Virtual Assistant Voice group in the Call Studio Elements . This element is an extension of the Form element and it engages the special resource on VVB called Speech Server to communicate with the Dialogflow Server.

The DialogflowCX element works with both Cisco DTMF and Nuance adaptors.

The DialogflowCX element supports both Speech and DTMF inputs.

In Cisco Contact Center Enterprise (CCE) Release 12.6(2) and later, the DialogflowCX element forwards SIP headers by default. To prevent forwarding SIP headers, configure the custom VXML property com.cisco.sipHeadersRestricted within the DialogflowCX element.

## Settings

Name (Label)

Type

Required

Single Setting Value

Substitution Allowed

Default

Notes

Config ID

String

No

true

true

None

Config ID is generated in Webex Control Hub as part of Virtual Agent–Voice onboarding.

If no Config ID is provided, the default config is fetched from the Control Hub.

Important

The default config in the Control Hub must point to the CX project.

Secure Logging

Boolean

Yes

true

true

false

Indicates whether logging of potentially sensitive data of the element is enabled. If set to, true the element's output data (query text , fulfilment text, and json) received from Google gets masked.

## Element Data

Element Data

Type

Notes

query_text

String

Transcription of the user utterance received as a response from Google ASR. This field is auto-populated.

fulfilment_text

String

Fulfillment text returned by Dialogflow CX. Multiple response text messages are concatenated as a single string value.

json

String

Contains raw JSON response as received from Google Dialogflow CX.

Use this element data for debug purposes only.

is_endof_session

Boolean

The value true indicates end of session.

is_live_agent_handoff

Boolean

The value true indicates live agent handoff.

is_custom_exit

Boolean

The value true indicates hybrid/custom exit from Dialogflow CX.

custom_payload

String

Contains the custom payload from Dialogflow CX with the Data parameters.

custom_event_name

String

Contains the event name from Dialogflow CX.

The custom event name can be overridden if required, by adding an element data event_name in the DialogflowCX element with the desired name. The same name should be configured at the CX Agent to re-enter the flow.

error_code

Int

The value contains the error code returned, to handle the call gracefully. The error scenarios are as follows:

Customer quota exhausted with Google.

DF CX service down or network is poor.

Error on Client creation towards Dialogflow CX.

## Exit States

Name

Notes

done

This state is returned after receiving response from Dialogflow CX. This indicates that the processing from Dialogflow has
                                       been completed.

Important

It is mandatory to return this state in order to continue with multiple dialogues.

error

This state is returned after the error response is received from Dialogflow CX. This indicates that the error has been encountered
                                       on the gRPC side.

## Custom VoiceXML Properties

Name (Label)

Type

Notes

Dialogflow.session.params.<param_name>

String

Sets the session parameter in CX at the start of the call.

Recognize.model

String

Contains the model name. The default value is null .

Recognize.modelVariant

String

Contains the model variant name. The following 4 values are supported as model variant name:

USE_STANDARD

SPEECH_MODEL_VARIANT_UNSPECIFIED

USE_ENHANCED

USE_BEST_AVAILABLE (default)

com.cisco.tts-server

String

This property is to be assigned the value "cloudTTS" , for transiting to the cloud.

| Note | The DialogflowCX element works with both Cisco DTMF and Nuance adaptors. The DialogflowCX element supports both Speech and DTMF inputs. |
|---|---|

| Name (Label) | Type | Required | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Config ID | String | No | true | true | None | Config ID is generated in Webex Control Hub as part of Virtual Agent–Voice onboarding. If no Config ID is provided, the default config is fetched from the Control Hub. Important The default config in the Control Hub must point to the CX project. | Important | The default config in the Control Hub must point to the CX project. |
| Important | The default config in the Control Hub must point to the CX project. |
| Secure Logging | Boolean | Yes | true | true | false | Indicates whether logging of potentially sensitive data of the element is enabled. If set to, true the element's output data (query text , fulfilment text, and json) received from Google gets masked. |

| Important | The default config in the Control Hub must point to the CX project. |
|---|---|

| Element Data | Type | Notes |
|---|---|---|
| query_text | String | Transcription of the user utterance received as a response from Google ASR. This field is auto-populated. |
| fulfilment_text | String | Fulfillment text returned by Dialogflow CX. Multiple response text messages are concatenated as a single string value. |
| json | String | Contains raw JSON response as received from Google Dialogflow CX. Note Use this element data for debug purposes only. | Note | Use this element data for debug purposes only. |
| Note | Use this element data for debug purposes only. |
| is_endof_session | Boolean | The value true indicates end of session. |
| is_live_agent_handoff | Boolean | The value true indicates live agent handoff. |
| is_custom_exit | Boolean | The value true indicates hybrid/custom exit from Dialogflow CX. |
| custom_payload | String | Contains the custom payload from Dialogflow CX with the Data parameters. |
| custom_event_name | String | Contains the event name from Dialogflow CX. Note The custom event name can be overridden if required, by adding an element data event_name in the DialogflowCX element with the desired name. The same name should be configured at the CX Agent to re-enter the flow. | Note | The custom event name can be overridden if required, by adding an element data event_name in the DialogflowCX element with the desired name. The same name should be configured at the CX Agent to re-enter the flow. |
| Note | The custom event name can be overridden if required, by adding an element data event_name in the DialogflowCX element with the desired name. The same name should be configured at the CX Agent to re-enter the flow. |
| error_code | Int | The value contains the error code returned, to handle the call gracefully. The error scenarios are as follows: Customer quota exhausted with Google. DF CX service down or network is poor. Error on Client creation towards Dialogflow CX. |

| Note | Use this element data for debug purposes only. |
|---|---|

| Note | The custom event name can be overridden if required, by adding an element data event_name in the DialogflowCX element with the desired name. The same name should be configured at the CX Agent to re-enter the flow. |
|---|---|

| Name | Notes |
|---|---|
| done | This state is returned after receiving response from Dialogflow CX. This indicates that the processing from Dialogflow has
                                       been completed. Important It is mandatory to return this state in order to continue with multiple dialogues. | Important | It is mandatory to return this state in order to continue with multiple dialogues. |
| Important | It is mandatory to return this state in order to continue with multiple dialogues. |
| error | This state is returned after the error response is received from Dialogflow CX. This indicates that the error has been encountered
                                       on the gRPC side. |

| Important | It is mandatory to return this state in order to continue with multiple dialogues. |
|---|---|

| Name (Label) | Type | Notes |
|---|---|---|
| Dialogflow.session.params.<param_name> | String | Sets the session parameter in CX at the start of the call. |
| Recognize.model | String | Contains the model name. The default value is null . |
| Recognize.modelVariant | String | Contains the model variant name. The following 4 values are supported as model variant name: USE_STANDARD SPEECH_MODEL_VARIANT_UNSPECIFIED USE_ENHANCED USE_BEST_AVAILABLE (default) |
| com.cisco.tts-server | String | This property is to be assigned the value "cloudTTS" , for transiting to the cloud. |