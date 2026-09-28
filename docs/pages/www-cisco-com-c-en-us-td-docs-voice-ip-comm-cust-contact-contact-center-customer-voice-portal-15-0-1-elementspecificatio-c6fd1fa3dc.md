---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-elementspecificatio-c6fd1fa3dc
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/elementspecification/guide/ccvp_b_150-element-specifications-guide-for-cvp-vxml-and-call-studio/subdialog_start.html
retrieved_at: 2026-08-21T17:12:37.460138+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

Updated: April 30, 2025

Chapter: Subdialog Start

## Chapter: Subdialog Start

# Subdialog Start

In most situations, the CVP Subdialog Start element (see CVP Subdialog Start ) should be used instead of this one , to offer full
                                    compatibility with ICM. However, there is one exception to
                                    this. If the voice application will only be called by a Subdialog Invoke element (that is, never by ICM),
                                    then the Subdialog Start and Subdialog
                                       Return elements may be used instead.

Data can be passed to the VoiceXML application either as HTTP parameters or VoiceXML parameters
                                    (using the <param> tag). In
                                    the first case (that is, as HTTP parameters), Call
                                    Services will automatically create session data
                                    using the name of the data received. In the second
                                    case (that is, as VoiceXML parameters), the
                                    Subdialog Start element must be configured
                                    appropriately in order for the data to be
                                    available as element or session data for the
                                    duration of the call session. For each data passed
                                    as a VoiceXML parameter, the repeatable Parameter setting must be
                                    configured with the same exact name as the data.

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
                                          match the exact value specified in the calling dialog. This is a repeatable
                                          setting, so multiple values can be specified.

Store As

(Store As)

string

No

false

false

Session Data

Set to Session Data to store the listed parameters in
                                          Session data, or to Element Data to store them in
                                          Element data.

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

com.audium.server.voiceElement.internal.DefaultSubdialogStartElement

| In most situations, the CVP Subdialog Start element (see CVP Subdialog Start ) should be used instead of this one , to offer full
                                    compatibility with ICM. However, there is one exception to
                                    this. If the voice application will only be called by a Subdialog Invoke element (that is, never by ICM),
                                    then the Subdialog Start and Subdialog
                                       Return elements may be used instead. Data can be passed to the VoiceXML application either as HTTP parameters or VoiceXML parameters
                                    (using the <param> tag). In
                                    the first case (that is, as HTTP parameters), Call
                                    Services will automatically create session data
                                    using the name of the data received. In the second
                                    case (that is, as VoiceXML parameters), the
                                    Subdialog Start element must be configured
                                    appropriately in order for the data to be
                                    available as element or session data for the
                                    duration of the call session. For each data passed
                                    as a VoiceXML parameter, the repeatable Parameter setting must be
                                    configured with the same exact name as the data. |
|---|

| Name
                                             (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Parameter (Parameter) | string | No | false | true | None | Holds the name of a parameter passed as input to the subdialog. It must
                                          match the exact value specified in the calling dialog. This is a repeatable
                                          setting, so multiple values can be specified. |
| Store As (Store As) | string | No | false | false | Session Data | Set to Session Data to store the listed parameters in
                                          Session data, or to Element Data to store them in
                                          Element data. |

| Name | Notes |
|---|---|
| done | The element is successfully run. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| General | com.audium.server.voiceElement.internal.DefaultSubdialogStartElement |