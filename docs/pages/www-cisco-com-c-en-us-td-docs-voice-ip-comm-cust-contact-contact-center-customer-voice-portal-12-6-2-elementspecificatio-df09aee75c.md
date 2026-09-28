---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-elementspecificatio-df09aee75c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/elementspecification/guide/ccvp_b_1262-element-specifications-guide/ccvp_mp_cfad8ed7_00_cvp-subdialog-start.html
retrieved_at: 2026-08-21T17:18:31.411375+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

Updated: April 28, 2023

Chapter: CVP Subdialog Start

## Chapter: CVP Subdialog Start

# CVP Subdialog Start

For a Cisco CVP voice
                                    application invoked as a subdialog, the CVP Subdialog
                                       Start element must be used, which receives data from a calling
                                    application and creates corresponding element data or session data. The element
                                    should be placed at the entrance point of the application, immediately after
                                    the Start of Call element.

Data can be passed to the VoiceXML
                                    application either as HTTP parameters or VoiceXML parameters (using the <param> tag). In the first case (that is, as
                                    HTTP parameters), Cisco Unified CVP VoiceXML Server will automatically create
                                    session data using the name of the data received. In the second case (that is,
                                    as VoiceXML parameters), the CVP Subdialog_Start element must be configured appropriately in order for the data to be available
                                    as element or session data for the duration of the call session. For each data
                                    passed as a VoiceXML parameter, the Parameter setting must
                                    be configured with the same exact name as the data. The Store
                                       As setting can be configured to store the passed data either as
                                    session or element data. The Enable Digits Bypass setting is used to activate a VoiceXML workaround to ensure expected
                                    functionality for a particular TDM or analog phone. When this setting is set to true , a new setting named Audio Filler
                                       URI will be enabled in VoiceXML Studio and can be configured to
                                    set a reference to a silence wave file to be played in the digits field. For IP
                                    phones the Enable Digits Bypass setting should be
                                    set to false .

## Settings

Name
                                             (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

Parameter

(Parameter)

string

No

false

true

None

Holds the name of a parameter passed as input to the subdialog. It must
                                          match the exact value specified in the VoiceXML page that calls the subdialog.
                                          This is a repeatable setting, so multiple values can be
                                          specified.

Where

(Store As)

string

No

true

false

Session Data

Determines whether the parameter passed to the subdialog will be stored
                                          as element data or session data. By making it element data, the information
                                          will "belong" only to this element, and so there is no chance that these
                                          variables will overwrite any other variables.

enable_digits_bypass

(Enable Digits
                                          Bypass)

boolean

Yes

true

true

false

Determines whether the digits field is used at the beginning of an
                                          application. By default this is disabled.

audio_filler_uri

(Audio Filler URI)

string

No

true

true

None

Configures a URI for a silence wave file to be played in the above digits
                                          field.

## Exit States

Name

Notes

done

The element is successfully run.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Cisco

com.audium.server.voiceElement.internal.CiscoSubdialogStartElement

| For a Cisco CVP voice
                                    application invoked as a subdialog, the CVP Subdialog
                                       Start element must be used, which receives data from a calling
                                    application and creates corresponding element data or session data. The element
                                    should be placed at the entrance point of the application, immediately after
                                    the Start of Call element. Data can be passed to the VoiceXML
                                    application either as HTTP parameters or VoiceXML parameters (using the <param> tag). In the first case (that is, as
                                    HTTP parameters), Cisco Unified CVP VoiceXML Server will automatically create
                                    session data using the name of the data received. In the second case (that is,
                                    as VoiceXML parameters), the CVP Subdialog_Start element must be configured appropriately in order for the data to be available
                                    as element or session data for the duration of the call session. For each data
                                    passed as a VoiceXML parameter, the Parameter setting must
                                    be configured with the same exact name as the data. The Store
                                       As setting can be configured to store the passed data either as
                                    session or element data. The Enable Digits Bypass setting is used to activate a VoiceXML workaround to ensure expected
                                    functionality for a particular TDM or analog phone. When this setting is set to true , a new setting named Audio Filler
                                       URI will be enabled in VoiceXML Studio and can be configured to
                                    set a reference to a silence wave file to be played in the digits field. For IP
                                    phones the Enable Digits Bypass setting should be
                                    set to false . |
|---|

| Name
                                             (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Parameter (Parameter) | string | No | false | true | None | Holds the name of a parameter passed as input to the subdialog. It must
                                          match the exact value specified in the VoiceXML page that calls the subdialog.
                                          This is a repeatable setting, so multiple values can be
                                          specified. |
| Where (Store As) | string | No | true | false | Session Data | Determines whether the parameter passed to the subdialog will be stored
                                          as element data or session data. By making it element data, the information
                                          will "belong" only to this element, and so there is no chance that these
                                          variables will overwrite any other variables. |
| enable_digits_bypass (Enable Digits
                                          Bypass) | boolean | Yes | true | true | false | Determines whether the digits field is used at the beginning of an
                                          application. By default this is disabled. |
| audio_filler_uri (Audio Filler URI) | string | No | true | true | None | Configures a URI for a silence wave file to be played in the above digits
                                          field. |

| Name | Notes |
|---|---|
| done | The element is successfully run. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Cisco | com.audium.server.voiceElement.internal.CiscoSubdialogStartElement |