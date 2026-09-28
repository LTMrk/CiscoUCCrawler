---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-elementspecificatio-99fabb61c2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/elementspecification/guide/ccvp_b_1262-element-specifications-guide/ccvp_mp_sa0dc43d_00_subdialog-return.html
retrieved_at: 2026-08-21T17:20:37.693446+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

Updated: April 28, 2023

Chapter: Subdialog Return

## Chapter: Subdialog Return

# Subdialog Return

In most situations, the CVP Subdialog Return element (see CVP Subdialog Return ) should be used instead of this one , to offer full compatibility
                                    with ICM. However, there is one exception to this. If the voice
                                    application will only be called by a Subdialog Invoke element (that
                                    is, never by ICM), then the Subdialog Start and Subdialog Return elements may be used instead. In this
                                    scenario, using this element allows an arbitrary number of return values to
                                    be retrieved from the subdialog, whereas the CVP Subdialog
                                       Return element allows only four.

## Settings

Name
                                             (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

return_value

(Return Value)

string

No

false

true

None

Optional return argument that holds a name/value pair to be returned to
                                          the calling application. The format should be: the name of the argument
                                          followed by an equal sign and the value of the argument. For example; name=John Doe . The element will take the text up to the
                                          first equal sign to be the name of the argument and the text following the
                                          equal sign to the
                                          value.

The following characters are not allowed in the return argument:

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

General

com.audium.server.voiceElement.internal.DefaultSubdialogReturnElement

| In most situations, the CVP Subdialog Return element (see CVP Subdialog Return ) should be used instead of this one , to offer full compatibility
                                    with ICM. However, there is one exception to this. If the voice
                                    application will only be called by a Subdialog Invoke element (that
                                    is, never by ICM), then the Subdialog Start and Subdialog Return elements may be used instead. In this
                                    scenario, using this element allows an arbitrary number of return values to
                                    be retrieved from the subdialog, whereas the CVP Subdialog
                                       Return element allows only four. |
|---|

| Name
                                             (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| return_value (Return Value) | string | No | false | true | None | Optional return argument that holds a name/value pair to be returned to
                                          the calling application. The format should be: the name of the argument
                                          followed by an equal sign and the value of the argument. For example; name=John Doe . The element will take the text up to the
                                          first equal sign to be the name of the argument and the text following the
                                          equal sign to the
                                          value. |

| Note | The following characters are not allowed in the return argument: < > " ' & |
|---|---|

| Name | Notes |
|---|---|
| done | The element is successfully run. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| General | com.audium.server.voiceElement.internal.DefaultSubdialogReturnElement |