---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-elementspecificatio-c708af1b76
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/elementspecification/guide/ccvp_b_150-element-specifications-guide-for-cvp-vxml-and-call-studio/virtualagentvoice.html
retrieved_at: 2026-08-21T17:13:04.922236+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

Updated: April 30, 2025

Chapter: VirtualAgentVoice

## Chapter: VirtualAgentVoice

# VirtualAgentVoice

The VirtualAgentVoice element is used to engage the Cisco Contact Center Artificial Intelligence (CCAI) services through the Cisco CCAI connector.
                                    The VirtualAgentVoice element is located under the Virtual Agent group in the Call Studio Elements . This element is an extension of the Form element and engages the special resource, Speech Server on Cisco VVB to communicate with the CCAI services.

VirtualAgentVoice element works only in VoiceXML 2.1 with Cisco DTMF and Nuance adapters.

VirtualAgentVoice element supports both Speech and DTMF inputs.

After an exit from the element, you must loop through the same element to continue the flow at the virtual agent provider
                                                      service.

If the welcome or re-entry prompt takes longer than the initial wait time (defined by the VXML property com.cisco.voicebrowser.welcomeLatencyInitialWait ), you can configure a prompt ( com.cisco.voicebrowser.welcomeLatencyPromptURL ) and play it in a loop until the welcome or re-entry prompt is received.

If an Audio prompt occurs before the VAV element in the call flow,  you must always mark it as non-barginable.

## Settings

Name (Label)

Type

Required

Single Setting Value

Substitution Allowed

Default

Notes

Connector Type

string

enum

Yes

true

false

Webex CCAI

Specifies the type of connector to be used for Virtual Agent Voice.

Webex CCAI : Webex AI Agent (Scripted or Autonomous AI Agent bots).

Integration : Any external vendor in partnership with Cisco such as Google.

For example: Select the Connector Type as Webex CCAI , if you are using Webex AI Agent as the connector type.

Virtual Agent

string

enum

Yes

true

false

Scripted

The type of the Virtual Agent Voice to be selected based on the behaviour.

Supported values are:

Scripted : AI Agents that rely on predefined intents and responses to handle customer interactions.

Autonomous : An advanced AI Agent designed to handle complex customer interactions using knowledge base and Large Language Models (LLMs).

For example, if you are using Google, configured with Connector Type as Integration, select the Virtual Agent as Scripted .

Agent ID

String

No

true

true

None

A mandatory field enabled when the Connector Type is selected as Webex CCAI .

For Webex AI Agent, only the Agent ID is required, which is available in the AI Agent Studio for the application.

Config ID

String

No

true

true

None

Config ID (Feature ID) can be created and managed from Control Hub.

This is required when using Connector Type as Integration or Service App .

Secure Logging

Boolean

Yes

true

true

false

Indicates whether the logging of potentially sensitive data of the element is enabled. If set to true , the element's output data ( query text and fulfilment text ) received from Google is masked.

Event Name

String

No

true

true

null

Event Name to be configured as start event or re-entry event.

Event Data

String

No

true

true

null

Contains the Name_Value_Table parameters for the session context.

Sip Headers Restricted

String

No

true

true

null

Contains the comma-separated list of SIP headers that must be excluded from propagating to the orchestration layer.

The SIP header names must be as per the RFC or Cisco-specified custom headers naming convention.

If the value of Sip Headers Restricted is null, or if it is unspecified, all the headers flow through the Orchestrator.

## Element Data

Element Data

Type

Notes

query_text

String

Transcription of the user utterance received as response from the ASR service. This field is auto-populated.

fulfillment_text

String

Fulfillment text returned by the Orchestrator. Multiple response text messages are concatenated as a single string value.

isCustomExit

Boolean

The value true indicates hybrid/custom exit from the cloud service, based on the presence of Execute_Request in the payload.

agent_handoff

String

If this element data exists, it means that the agent handoff has happened and it may contain metadata.

end_session

String

If this element data exists, it means that the end of session has happened and it may contain metadata.

eventName

String

Contains the event name from the cloud service as a part of the hybrid handoff.

eventData

String

Contains the custom payload from the cloud service as a part of the hybrid handoff.

error_code

Int

The value contains the error code returned to handle the call gracefully.

## Exit States

Name

Notes

done

Indicates that the processing from the cloud service has been completed. After a response is received from the orchestration
                                       layer, this state is returned.

error

This state is returned after the error response is received from the orchestration layer. This indicates that the error has
                                       been encountered on the gRPC side.

VXML Event - noresource

This exit state is used to handle scenarios where resources are not available to process the call.

VXML Event - badfetch

This exit state ensures a controlled call flow, even in cases where agent responses are missing.

To define an exit state:

Add an event with Event Type set to VXML Event .

Select error.badfetch from the event list.

To avoid the VXML Event - badfetch, ensure seamless integration of the VirtualAgentVoice element with the Google DialogflowCX
                           Agent by including at least one of the following components in each dialogue response

Output audio text (with or without SSML)

Pre-recorded audio playback

Agent responses can incorporate multiple instances of Output audio text and Pre-recorded audio in any order. However, Output
                           audio text should not be empty or consist only of spaces.

If the DialogflowCX Agent lacks a dialogue with a defined agent response, the call flow associated with the VirtualAgentVoice
                           element will terminate with an error.badfetch. This avoids unwanted silence and ensures that agent responses are properly
                           defined in the Google DialogflowCX Agent. Therefore, it is recommended to provide agent responses for every dialogue to avoid
                           call flow termination due to error.badfetch.

If managing error.badfetch gracefully is preferred over defining responses for every dialogue, the VirtualAgentVoice element
                           can handle this error similar to error.noresource.

## Custom VoiceXML Properties

Name (Label)

Type

Notes

Recognize.model

String

Contains the model name. The default value is null .

Recognize.modelVariant

String

Contains the model variant name.

For example, the following 4 values are supported as model variant name for Dialogflow CX:

USE_STANDARD

SPEECH_MODEL_VARIANT_UNSPECIFIED

USE_ENHANCED

USE_BEST_AVAILABLE (default)

com.cisco.voicebrowser.welcome

LatencyPromptURL

String

URL of the prompt to be played during welcome /re-entry prompt fetch to avoid dead air.

Supports both http (remote) and crtp (local) prompts. However, l ocal prompts are recommended.

com.cisco.voicebrowser.welcome

LatencyInitialWait

Integer > 0

Initial wait time (in ms) to play the prompt configured in com.cisco.voicebrowser.welcomeLatencyPromptURL .

The default value is 5000 ms.

com.cisco.voicebrowser.welcome

maxwaittime

Integer > 0

Maximum wait time (in ms) for receiving a welcome response. If the response for welcome event is not received within this
                                       time, an error is thrown and the call is disconnected.

The default value is 15000 ms, if nothing is specified in the Call Studio application.

com.cisco.responseThreshold

Integer > 0

Threshold wait time to receive the welcome response from the server. If the welcome response is not received within this time,
                                       a syslog alarm is raised.

The default value is 5000 ms.

com.cisco.language

String

Contains the language format which will be used for playing the prompts, such as "en-US".

com.cisco.AIAgent.MetaData.DynamicWelcomeMessage

String

For Webex AI Agent, when Autonomous agent is selected from drop-down list.

Adds support for dynamic_welcome_message = true. When this field is enabled, dynamic welcome message prompt is played at the
                                       start of the bot.

The default value is false , if nothing is specified in the Call Studio application.

| The VirtualAgentVoice element is used to engage the Cisco Contact Center Artificial Intelligence (CCAI) services through the Cisco CCAI connector.
                                    The VirtualAgentVoice element is located under the Virtual Agent group in the Call Studio Elements . This element is an extension of the Form element and engages the special resource, Speech Server on Cisco VVB to communicate with the CCAI services. Note VirtualAgentVoice element works only in VoiceXML 2.1 with Cisco DTMF and Nuance adapters. VirtualAgentVoice element supports both Speech and DTMF inputs. After an exit from the element, you must loop through the same element to continue the flow at the virtual agent provider
                                                      service. If the welcome or re-entry prompt takes longer than the initial wait time (defined by the VXML property com.cisco.voicebrowser.welcomeLatencyInitialWait ), you can configure a prompt ( com.cisco.voicebrowser.welcomeLatencyPromptURL ) and play it in a loop until the welcome or re-entry prompt is received. If an Audio prompt occurs before the VAV element in the call flow,  you must always mark it as non-barginable. | Note | VirtualAgentVoice element works only in VoiceXML 2.1 with Cisco DTMF and Nuance adapters. VirtualAgentVoice element supports both Speech and DTMF inputs. After an exit from the element, you must loop through the same element to continue the flow at the virtual agent provider
                                                      service. If the welcome or re-entry prompt takes longer than the initial wait time (defined by the VXML property com.cisco.voicebrowser.welcomeLatencyInitialWait ), you can configure a prompt ( com.cisco.voicebrowser.welcomeLatencyPromptURL ) and play it in a loop until the welcome or re-entry prompt is received. If an Audio prompt occurs before the VAV element in the call flow,  you must always mark it as non-barginable. |
|---|---|---|
| Note | VirtualAgentVoice element works only in VoiceXML 2.1 with Cisco DTMF and Nuance adapters. VirtualAgentVoice element supports both Speech and DTMF inputs. After an exit from the element, you must loop through the same element to continue the flow at the virtual agent provider
                                                      service. If the welcome or re-entry prompt takes longer than the initial wait time (defined by the VXML property com.cisco.voicebrowser.welcomeLatencyInitialWait ), you can configure a prompt ( com.cisco.voicebrowser.welcomeLatencyPromptURL ) and play it in a loop until the welcome or re-entry prompt is received. If an Audio prompt occurs before the VAV element in the call flow,  you must always mark it as non-barginable. |

| Note | VirtualAgentVoice element works only in VoiceXML 2.1 with Cisco DTMF and Nuance adapters. VirtualAgentVoice element supports both Speech and DTMF inputs. After an exit from the element, you must loop through the same element to continue the flow at the virtual agent provider
                                                      service. If the welcome or re-entry prompt takes longer than the initial wait time (defined by the VXML property com.cisco.voicebrowser.welcomeLatencyInitialWait ), you can configure a prompt ( com.cisco.voicebrowser.welcomeLatencyPromptURL ) and play it in a loop until the welcome or re-entry prompt is received. If an Audio prompt occurs before the VAV element in the call flow,  you must always mark it as non-barginable. |
|---|---|

| Name (Label) | Type | Required | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Connector Type | string enum | Yes | true | false | Webex CCAI | Specifies the type of connector to be used for Virtual Agent Voice. Webex CCAI : Webex AI Agent (Scripted or Autonomous AI Agent bots). Integration : Any external vendor in partnership with Cisco such as Google. For example: Select the Connector Type as Webex CCAI , if you are using Webex AI Agent as the connector type. |
| Virtual Agent | string enum | Yes | true | false | Scripted | The type of the Virtual Agent Voice to be selected based on the behaviour. Supported values are: Scripted : AI Agents that rely on predefined intents and responses to handle customer interactions. Autonomous : An advanced AI Agent designed to handle complex customer interactions using knowledge base and Large Language Models (LLMs). For example, if you are using Google, configured with Connector Type as Integration, select the Virtual Agent as Scripted . |
| Agent ID | String | No | true | true | None | A mandatory field enabled when the Connector Type is selected as Webex CCAI . For Webex AI Agent, only the Agent ID is required, which is available in the AI Agent Studio for the application. |
| Config ID | String | No | true | true | None | Config ID (Feature ID) can be created and managed from Control Hub. Note This is required when using Connector Type as Integration or Service App . | Note | This is required when using Connector Type as Integration or Service App . |
| Note | This is required when using Connector Type as Integration or Service App . |
| Secure Logging | Boolean | Yes | true | true | false | Indicates whether the logging of potentially sensitive data of the element is enabled. If set to true , the element's output data ( query text and fulfilment text ) received from Google is masked. |
| Event Name | String | No | true | true | null | Event Name to be configured as start event or re-entry event. |
| Event Data | String | No | true | true | null | Contains the Name_Value_Table parameters for the session context. |
| Sip Headers Restricted | String | No | true | true | null | Contains the comma-separated list of SIP headers that must be excluded from propagating to the orchestration layer. The SIP header names must be as per the RFC or Cisco-specified custom headers naming convention. If the value of Sip Headers Restricted is null, or if it is unspecified, all the headers flow through the Orchestrator. |

| Note | This is required when using Connector Type as Integration or Service App . |
|---|---|

| Element Data | Type | Notes |
|---|---|---|
| query_text | String | Transcription of the user utterance received as response from the ASR service. This field is auto-populated. |
| fulfillment_text | String | Fulfillment text returned by the Orchestrator. Multiple response text messages are concatenated as a single string value. |
| isCustomExit | Boolean | The value true indicates hybrid/custom exit from the cloud service, based on the presence of Execute_Request in the payload. |
| agent_handoff | String | If this element data exists, it means that the agent handoff has happened and it may contain metadata. |
| end_session | String | If this element data exists, it means that the end of session has happened and it may contain metadata. |
| eventName | String | Contains the event name from the cloud service as a part of the hybrid handoff. |
| eventData | String | Contains the custom payload from the cloud service as a part of the hybrid handoff. |
| error_code | Int | The value contains the error code returned to handle the call gracefully. |

| Name | Notes |
|---|---|
| done | Indicates that the processing from the cloud service has been completed. After a response is received from the orchestration
                                       layer, this state is returned. |
| error | This state is returned after the error response is received from the orchestration layer. This indicates that the error has
                                       been encountered on the gRPC side. |
| VXML Event - noresource | This exit state is used to handle scenarios where resources are not available to process the call. |
| VXML Event - badfetch | This exit state ensures a controlled call flow, even in cases where agent responses are missing. To define an exit state: Add an event with Event Type set to VXML Event . Select error.badfetch from the event list. |

| Name (Label) | Type | Notes |
|---|---|---|
| Recognize.model | String | Contains the model name. The default value is null . |
| Recognize.modelVariant | String | Contains the model variant name. For example, the following 4 values are supported as model variant name for Dialogflow CX: USE_STANDARD SPEECH_MODEL_VARIANT_UNSPECIFIED USE_ENHANCED USE_BEST_AVAILABLE (default) |
| com.cisco.voicebrowser.welcome LatencyPromptURL | String | URL of the prompt to be played during welcome /re-entry prompt fetch to avoid dead air. Supports both http (remote) and crtp (local) prompts. However, l ocal prompts are recommended. |
| com.cisco.voicebrowser.welcome LatencyInitialWait | Integer > 0 | Initial wait time (in ms) to play the prompt configured in com.cisco.voicebrowser.welcomeLatencyPromptURL . The default value is 5000 ms. |
| com.cisco.voicebrowser.welcome maxwaittime | Integer > 0 | Maximum wait time (in ms) for receiving a welcome response. If the response for welcome event is not received within this
                                       time, an error is thrown and the call is disconnected. The default value is 15000 ms, if nothing is specified in the Call Studio application. |
| com.cisco.responseThreshold | Integer > 0 | Threshold wait time to receive the welcome response from the server. If the welcome response is not received within this time,
                                       a syslog alarm is raised. The default value is 5000 ms. |
| com.cisco.language | String | Contains the language format which will be used for playing the prompts, such as "en-US". |
| com.cisco.AIAgent.MetaData.DynamicWelcomeMessage | String | For Webex AI Agent, when Autonomous agent is selected from drop-down list. Adds support for dynamic_welcome_message = true. When this field is enabled, dynamic welcome message prompt is played at the
                                       start of the bot. The default value is false , if nothing is specified in the Call Studio application. |