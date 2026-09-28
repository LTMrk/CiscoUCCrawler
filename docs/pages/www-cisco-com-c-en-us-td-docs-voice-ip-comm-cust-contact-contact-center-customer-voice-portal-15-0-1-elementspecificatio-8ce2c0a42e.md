---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-elementspecificatio-8ce2c0a42e
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/elementspecification/guide/ccvp_b_150-element-specifications-guide-for-cvp-vxml-and-call-studio/subdialog_invoke.html
retrieved_at: 2026-08-21T17:12:28.975425+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

Updated: April 30, 2025

Chapter: Subdialog Invoke

## Chapter: Subdialog Invoke

# Subdialog Invoke

The Subdialog Invoke element initiates a subdialog
                                    invocation to another VoiceXML application, and handles passing data to and
                                    from the application. For the entire duration while a subdialog application
                                    is handling a call, the calling application waits in a dormant state for the
                                    subdialog to return. The goal of the Subdialog Invoke element is to allow
                                    voice applications to be invoked across multiple servers, as well as giving
                                    temporary control of the call to a voice application (such as flat VoiceXML
                                    and JSPs) created outside Call Studio.

## Settings

Name (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

subdialog_uri

(Subdialog URI)

string

Yes

true

true

None

Specifies the URI of the subdialog to invoke. This may either be
                                          				  a relative or absolute URI, but must be accessible to the voice browser at
                                          				  runtime.

local_application

(Local Application)

boolean

Yes

true

true

None

Specifies whether or not the subdialog application is running on
                                          				  the same application server as the application in which the current element
                                          				  appears.

parameter

(Parameter)

string

No

false

true

None

Holds the name and value of a parameter to pass to the
                                          				  subdialog. The format is the name of the parameter followed by an equal sign
                                          				  (=) followed by the value of the parameter. For example: name=John Doe . The element will use the text up to the
                                          				  first equal sign as the name of the parameter and the remaining text as the
                                          				  value .

return_value

(Return Value)

string

No

false

true

None

Holds the name of a return value from the subdialog. For
                                          				  example: result . The names specified here must match the variable
                                          				  names returned by the subdialog. Return values will be stored as element data,
                                          				  in a variable of the name specified here.

## Exit States

Name

Notes

done

The element is successfully run.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

General

com.audium.server.voiceElement.internal.SubdialogInvoke

## Events

Name (Label)

Notes

Event Type

The VXML
                                          				  Event handler type is available for this element.

| The Subdialog Invoke element initiates a subdialog
                                    invocation to another VoiceXML application, and handles passing data to and
                                    from the application. For the entire duration while a subdialog application
                                    is handling a call, the calling application waits in a dormant state for the
                                    subdialog to return. The goal of the Subdialog Invoke element is to allow
                                    voice applications to be invoked across multiple servers, as well as giving
                                    temporary control of the call to a voice application (such as flat VoiceXML
                                    and JSPs) created outside Call Studio. |
|---|

| Name (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| subdialog_uri (Subdialog URI) | string | Yes | true | true | None | Specifies the URI of the subdialog to invoke. This may either be
                                          				  a relative or absolute URI, but must be accessible to the voice browser at
                                          				  runtime. |
| local_application (Local Application) | boolean | Yes | true | true | None | Specifies whether or not the subdialog application is running on
                                          				  the same application server as the application in which the current element
                                          				  appears. |
| parameter (Parameter) | string | No | false | true | None | Holds the name and value of a parameter to pass to the
                                          				  subdialog. The format is the name of the parameter followed by an equal sign
                                          				  (=) followed by the value of the parameter. For example: name=John Doe . The element will use the text up to the
                                          				  first equal sign as the name of the parameter and the remaining text as the
                                          				  value . |
| return_value (Return Value) | string | No | false | true | None | Holds the name of a return value from the subdialog. For
                                          				  example: result . The names specified here must match the variable
                                          				  names returned by the subdialog. Return values will be stored as element data,
                                          				  in a variable of the name specified here. |

| Name | Notes |
|---|---|
| done | The element is successfully run. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| General | com.audium.server.voiceElement.internal.SubdialogInvoke |

| Name (Label) | Notes |
|---|---|
| Event Type | The VXML
                                          				  Event handler type is available for this element. |