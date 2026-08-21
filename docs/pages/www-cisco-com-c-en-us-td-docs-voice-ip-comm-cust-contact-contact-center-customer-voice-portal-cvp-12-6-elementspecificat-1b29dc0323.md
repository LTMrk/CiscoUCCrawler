---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-elementspecificat-1b29dc0323
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/elementspecification/guide/ccvp_b_1261-element-specifications-guide/ccvp_mp_a09b5daf_00_application_modifier.html
retrieved_at: 2026-08-21T17:23:16.429142+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

Updated: February 18, 2020

Chapter: Application_Modifier

## Chapter: Application_Modifier

# Application_Modifier

The Application_Modifier action element is used to
                                    modify context variables and remove session data values at runtime in a voice
                                    application. It allows for a developer to change the application’s environment
                                    anywhere in the callflow. A typical use for the Application_Modifier element
                                    would be for multi-language support because it can be used to change the
                                    application level xml:lang and encoding values.
                                    Visiting an Application_Modifier element instance will update the application
                                    for the current session
                                    only.

## Settings

Name
                                             (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

maintainer

(Maintainer)

string

No

true

true

None

This
                                          setting specifies the e-mail address of the voice application administrator.
                                          This value is set in a VoiceXML <meta> tag.

language

(Language)

string

No

true

true

None

This setting specifies the language identifier to
                                          specify in each VoiceXML document's xml:lang attribute. This value is set in the <vxml> tag.

encoding

(Encoding)

string

No

true

true

None

This setting specifies the encoding to use when
                                          creating VoiceXML documents. This value is set in the <xml> tag.

default_audio_path

(Default Audio
                                          Path)

string

No

true

true

None

This
                                          setting specifies a partial URI to a path containing the audio content for this
                                          voice application.

remove_session_data

(Session Data to Remove)

string

No

false

true

None

This
                                          setting specifies the names of session data values to remove from this voice
                                          application.

Voice Name

String

No

true

true

None

This can take voice names provided by Google. For more information see https://cloud.google.com/text-to-speech/docs/voices

## Exit States

Name

Notes

done

The
                                          application’s context variables were modified and session data values were
                                          removed.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Context

com.audium.server.action.context.ApplicationModifier

## Events

Name (Label)

Notes

Event Type

You can
                                          				  select Java Exception as event handler type.

The output of the Customer_Lookup element can be in JSON format . To know more about parsing the JSON Data refer to "Parsing
                              JSON Data" section in User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio.

| The Application_Modifier action element is used to
                                    modify context variables and remove session data values at runtime in a voice
                                    application. It allows for a developer to change the application’s environment
                                    anywhere in the callflow. A typical use for the Application_Modifier element
                                    would be for multi-language support because it can be used to change the
                                    application level xml:lang and encoding values.
                                    Visiting an Application_Modifier element instance will update the application
                                    for the current session
                                    only. |
|---|

| Name
                                             (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| maintainer (Maintainer) | string | No | true | true | None | This
                                          setting specifies the e-mail address of the voice application administrator.
                                          This value is set in a VoiceXML <meta> tag. |
| language (Language) | string | No | true | true | None | This setting specifies the language identifier to
                                          specify in each VoiceXML document's xml:lang attribute. This value is set in the <vxml> tag. |
| encoding (Encoding) | string | No | true | true | None | This setting specifies the encoding to use when
                                          creating VoiceXML documents. This value is set in the <xml> tag. |
| default_audio_path (Default Audio
                                          Path) | string | No | true | true | None | This
                                          setting specifies a partial URI to a path containing the audio content for this
                                          voice application. |
| remove_session_data (Session Data to Remove) | string | No | false | true | None | This
                                          setting specifies the names of session data values to remove from this voice
                                          application. |
| Voice Name | String | No | true | true | None | This can take voice names provided by Google. For more information see https://cloud.google.com/text-to-speech/docs/voices |

| Name | Notes |
|---|---|
| done | The
                                          application’s context variables were modified and session data values were
                                          removed. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Context | com.audium.server.action.context.ApplicationModifier |

| Name (Label) | Notes |
|---|---|
| Event Type | You can
                                          				  select Java Exception as event handler type. |