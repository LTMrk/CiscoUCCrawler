---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-elementspecificatio-1410a12a4b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/elementspecification/guide/ccvp_b_150-element-specifications-guide-for-cvp-vxml-and-call-studio/cvp_subdialog_return.html
retrieved_at: 2026-08-21T17:10:31.271379+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

Updated: April 30, 2025

Chapter: CVP Subdialog Return

## Chapter: CVP Subdialog Return

# CVP Subdialog Return

For a Cisco Unified CVP Voice application invoked as a subdialog, the CVP Subdialog Return element must be used to return
                                    data back to the calling application. The element should be used in place of
                                    Hang Up elements throughout the call flow. Like a Hang Up element, the
                                    element has no exit states.

The settings for this element are used to define what data
                                    to pass back to the calling application. The Caller Input setting must be assigned a value in order for the application to validate,
                                    since it is required to have a value. Each element setting corresponds to an
                                    ICM ECC external variable name, and therefore the configuration values must
                                    conform to requirements associated with ICM ECC variables. Refer to the
                                    Unified CVP documentation for further details.

The CVP Subdialog
                                    Return element can be used to enable multiple types of transfer in call
                                    failure conditions. In case of a Hook Flash (HF) or Two B-Channel Transfer
                                    (TBCT) transfer, for example, Caller Input should be set to
                                    the transfer destination number prefixed with HF or TBCT (as
                                    in HF800xxxxxxx or TBCT800xxxxxxx). An HF or TBCT transfer will be invoked
                                    after the Caller Input was passed back from the CVP
                                    Subdialog Return element.

## Settings

Name
                                             (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

caller_input

(Caller Input)

string

Yes

true

true

None

Required return argument that holds a value to be returned to the calling
                                          application.

FromExtVXML0

(External VXML 0)

string

No

true

true

None

Optional return argument that is returned to the calling
                                          application.

FromExtVXML1

(External VXML 1)

string

No

true

true

None

Optional return argument that is returned to the
                                          calling application.

FromExtVXML2

(External VXML 2)

string

No

true

true

None

Optional return argument that is returned to the calling
                                          application.

FromExtVXML3

(External VXML 3)

string

No

true

true

None

Optional return argument that is returned to the
                                          calling
                                          application.

The following characters are not allowed in the return arguments:

< > " ' &

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

com.audium.server.voiceElement.internal.CiscoSubdialogReturnElement

| For a Cisco Unified CVP Voice application invoked as a subdialog, the CVP Subdialog Return element must be used to return
                                    data back to the calling application. The element should be used in place of
                                    Hang Up elements throughout the call flow. Like a Hang Up element, the
                                    element has no exit states. Note There is one exception to the above description. If the voice application will only ever be
                                             called by a Subdialog Invoke element (that is, never by Unified ICM), then
                                             the Subdialog Start and Subdialog Return elements may be used instead. Refer
                                             to The settings for this element are used to define what data
                                    to pass back to the calling application. The Caller Input setting must be assigned a value in order for the application to validate,
                                    since it is required to have a value. Each element setting corresponds to an
                                    ICM ECC external variable name, and therefore the configuration values must
                                    conform to requirements associated with ICM ECC variables. Refer to the
                                    Unified CVP documentation for further details. The CVP Subdialog
                                    Return element can be used to enable multiple types of transfer in call
                                    failure conditions. In case of a Hook Flash (HF) or Two B-Channel Transfer
                                    (TBCT) transfer, for example, Caller Input should be set to
                                    the transfer destination number prefixed with HF or TBCT (as
                                    in HF800xxxxxxx or TBCT800xxxxxxx). An HF or TBCT transfer will be invoked
                                    after the Caller Input was passed back from the CVP
                                    Subdialog Return element. | Note | There is one exception to the above description. If the voice application will only ever be
                                             called by a Subdialog Invoke element (that is, never by Unified ICM), then
                                             the Subdialog Start and Subdialog Return elements may be used instead. Refer
                                             to |
|---|---|---|
| Note | There is one exception to the above description. If the voice application will only ever be
                                             called by a Subdialog Invoke element (that is, never by Unified ICM), then
                                             the Subdialog Start and Subdialog Return elements may be used instead. Refer
                                             to |

| Note | There is one exception to the above description. If the voice application will only ever be
                                             called by a Subdialog Invoke element (that is, never by Unified ICM), then
                                             the Subdialog Start and Subdialog Return elements may be used instead. Refer
                                             to |
|---|---|

| Name
                                             (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| caller_input (Caller Input) | string | Yes | true | true | None | Required return argument that holds a value to be returned to the calling
                                          application. |
| FromExtVXML0 (External VXML 0) | string | No | true | true | None | Optional return argument that is returned to the calling
                                          application. |
| FromExtVXML1 (External VXML 1) | string | No | true | true | None | Optional return argument that is returned to the
                                          calling application. |
| FromExtVXML2 (External VXML 2) | string | No | true | true | None | Optional return argument that is returned to the calling
                                          application. |
| FromExtVXML3 (External VXML 3) | string | No | true | true | None | Optional return argument that is returned to the
                                          calling
                                          application. |

| Note | The following characters are not allowed in the return arguments: < > " ' & |
|---|---|

| Name | Notes |
|---|---|
| done | The element is successfully run. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Cisco | com.audium.server.voiceElement.internal.CiscoSubdialogReturnElement |