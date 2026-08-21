---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-reference-guide-c-4ad33bf638
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/reference/guide/ccvp_b_1251-element-specification-guide-cvp/ccvp_m_1251-wxm-pcs.html
retrieved_at: 2026-08-21T17:34:44.917102+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.5(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.5(1)

Updated: January 31, 2020

Chapter: WxM PCS

## Chapter: WxM PCS

# WxM PCS

The WxM PCS element can be used to engage Post Call Survey with Webex Experience Management. The WxM PCS element is located under the wxm group in the Call Studio Elements . This element is an extension of the Form element and connects with Webex Experience Management to play the configured survey questions through VVB.

## Settings

Name (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

NoInput Timeout

string

Yes

true

true

5s

The maximum time length allowed for silence or no keypress before a noinput event is thrown. Possible values are standard
                                          time designations including both a non-negative number and a time unit, for example, 3s (for seconds) or 300ms (for milliseconds).
                                          Default = 5s.

Max NoInput Count

int ≥ 0

Yes

true

true

3

The maximum number of noinput events allowed during input capture. Possible values int > 0. 0 = infinite noinputs allowed.

Max NoMatch Count

int ≥ 0

Yes

true

true

3

The maximum number of nomatch events allowed during input capture. Possible values int > 0. 0 = infinite match allowed.

Survey Name

string

No

true

Yes

WxM survey name to be played as a part of Post Call Survey. If this field is empty, it's value is retrieved from ICM.

Survey Token

string

No

true

Yes

WxM survey taken required to submit survey back to WxM. If this field is empty, it will be retrieved from WxM through api
                                          call.

Auth Token

string

No

true

true

WXM auth token.If the field is empty, auth token would be retrieved from WXM auth token API call.

Barge In

boolean

Yes

true

true

true

If the value is true then barge in is allowed.

Secure Logging

boolean

Yes

true

true

false

Whether or not to enable logging of potentially sensitive data of the element. If set to true, the element's potentially sensitive
                                          data will not log.

## Element Data

Name

Type

Notes

value

string

This field holds the questions and answers along with prefills in JSON format submitted to WXM.

## Exit States

Name

Notes

done

This state is returned after getting DTMF response for all the questions successfully.

max_noinput

The maximum number of noinput events occurred. If the noinput max count is 0, this exit state never occurs.

max_nomatch

The maximum number of nomatch events occurred. If the nomatch max count is 0, this exit state never occurs.

## Audio Group

### Form Data Capture

Name (Label)

Required

Max1

Notes

noinput_audio_group (NoInput)

No

No

Played when a NoInput event occurs.

1. If noinput_audio_group is not configured, question text is played to the user for configured number of times (Max NoInput Count).

2. If noinput_audio_group is configured, question text is not played if no input event occurs. Only the prompt in noinput_audio_group will be played.

nomatch_audio_group (NoMatch)

No

No

Played when a nomatch event occurs.

1. If nomatch_audio_group is not configured, question text is played to the user for configured number of times (Max NoMatch Count).

2. If nomatch_audio_group is configured, question text is not played if no match event occurs. Only the prompt in nomatch_audio_group will be played.

## Custom Prefills

The following Custom Prefills can be added from the Call Studio as element data in Data tab:

Name

Value

Substitution Allowed

Default

Name

Prefills tag from Cloud Cherry

No

empty

Value

Value of the prefill

Yes

empty

Type

Data type of the value

No

String

Create

No

Before

## Folder and Class Information

Studio Element Folder Name

Class Name

Form

com.audium.server.voiceElement.form

## Events

Name (Label)

Notes

Event Type

You can select Java Exception, VXML Event, or Hotlink, as event handler for this element.

| The WxM PCS element can be used to engage Post Call Survey with Webex Experience Management. The WxM PCS element is located under the wxm group in the Call Studio Elements . This element is an extension of the Form element and connects with Webex Experience Management to play the configured survey questions through VVB. |
|---|

| Name (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| NoInput Timeout | string | Yes | true | true | 5s | The maximum time length allowed for silence or no keypress before a noinput event is thrown. Possible values are standard
                                          time designations including both a non-negative number and a time unit, for example, 3s (for seconds) or 300ms (for milliseconds).
                                          Default = 5s. |
| Max NoInput Count | int ≥ 0 | Yes | true | true | 3 | The maximum number of noinput events allowed during input capture. Possible values int > 0. 0 = infinite noinputs allowed. |
| Max NoMatch Count | int ≥ 0 | Yes | true | true | 3 | The maximum number of nomatch events allowed during input capture. Possible values int > 0. 0 = infinite match allowed. |
| Survey Name | string | No | true | Yes |  | WxM survey name to be played as a part of Post Call Survey. If this field is empty, it's value is retrieved from ICM. |
| Survey Token | string | No | true | Yes |  | WxM survey taken required to submit survey back to WxM. If this field is empty, it will be retrieved from WxM through api
                                          call. |
| Auth Token | string | No | true | true |  | WXM auth token.If the field is empty, auth token would be retrieved from WXM auth token API call. |
| Barge In | boolean | Yes | true | true | true | If the value is true then barge in is allowed. |
| Secure Logging | boolean | Yes | true | true | false | Whether or not to enable logging of potentially sensitive data of the element. If set to true, the element's potentially sensitive
                                          data will not log. |

| Name | Type | Notes |
|---|---|---|
| value | string | This field holds the questions and answers along with prefills in JSON format submitted to WXM. |

| Name | Notes |
|---|---|
| done | This state is returned after getting DTMF response for all the questions successfully. |
| max_noinput | The maximum number of noinput events occurred. If the noinput max count is 0, this exit state never occurs. |
| max_nomatch | The maximum number of nomatch events occurred. If the nomatch max count is 0, this exit state never occurs. |

| Name (Label) | Required | Max1 | Notes |
|---|---|---|---|
| noinput_audio_group (NoInput) | No | No | Played when a NoInput event occurs. Note 1. If noinput_audio_group is not configured, question text is played to the user for configured number of times (Max NoInput Count). 2. If noinput_audio_group is configured, question text is not played if no input event occurs. Only the prompt in noinput_audio_group will be played. | Note | 1. If noinput_audio_group is not configured, question text is played to the user for configured number of times (Max NoInput Count). 2. If noinput_audio_group is configured, question text is not played if no input event occurs. Only the prompt in noinput_audio_group will be played. |
| Note | 1. If noinput_audio_group is not configured, question text is played to the user for configured number of times (Max NoInput Count). 2. If noinput_audio_group is configured, question text is not played if no input event occurs. Only the prompt in noinput_audio_group will be played. |
| nomatch_audio_group (NoMatch) | No | No | Played when a nomatch event occurs. Note 1. If nomatch_audio_group is not configured, question text is played to the user for configured number of times (Max NoMatch Count). 2. If nomatch_audio_group is configured, question text is not played if no match event occurs. Only the prompt in nomatch_audio_group will be played. | Note | 1. If nomatch_audio_group is not configured, question text is played to the user for configured number of times (Max NoMatch Count). 2. If nomatch_audio_group is configured, question text is not played if no match event occurs. Only the prompt in nomatch_audio_group will be played. |
| Note | 1. If nomatch_audio_group is not configured, question text is played to the user for configured number of times (Max NoMatch Count). 2. If nomatch_audio_group is configured, question text is not played if no match event occurs. Only the prompt in nomatch_audio_group will be played. |

| Note | 1. If noinput_audio_group is not configured, question text is played to the user for configured number of times (Max NoInput Count). 2. If noinput_audio_group is configured, question text is not played if no input event occurs. Only the prompt in noinput_audio_group will be played. |
|---|---|

| Note | 1. If nomatch_audio_group is not configured, question text is played to the user for configured number of times (Max NoMatch Count). 2. If nomatch_audio_group is configured, question text is not played if no match event occurs. Only the prompt in nomatch_audio_group will be played. |
|---|---|

| Name | Value | Substitution Allowed | Default |
|---|---|---|---|
| Name | Prefills tag from Cloud Cherry | No | empty |
| Value | Value of the prefill | Yes | empty |
| Type | Data type of the value | No | String |
| Create |  | No | Before |

| Studio Element Folder Name | Class Name |
|---|---|
| Form | com.audium.server.voiceElement.form |

| Name (Label) | Notes |
|---|---|
| Event Type | You can select Java Exception, VXML Event, or Hotlink, as event handler for this element. |