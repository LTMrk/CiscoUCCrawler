---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-elementspecificat-53ea556deb
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/elementspecification/guide/ccvp_b_1261-element-specifications-guide/ccvp_mp_c7502fa2_00_callback_wait.html
retrieved_at: 2026-08-21T17:24:02.225900+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

Updated: February 18, 2020

Chapter: Callback_Wait

## Chapter: Callback_Wait

# Callback_Wait

The Callback_Wait element is responsible for sleeping the application for X
                                    seconds. The application hands control back to cvp_ccb_vxml.tcl with the
                                    parameter
                                    wait=X.

## Settings

Name
                                             (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

Wait Time

integer

Yes

true

false

None

Amount of time in seconds to wait. Maximum is 60,
                                          minimum is 0.

## Exit States

Name

Notes

done

The element is successfully run and the value is retrieved.

error

The element failed to
                                          retrieve the
                                          value.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Cisco > Callback

com.cisco.cvp.vxml.custelem.callback.Wait

## Events

Name (Label)

Notes

Event Type

You can select Java Exception , VXML Event , or Hotlink as event handler for this element.

| The Callback_Wait element is responsible for sleeping the application for X
                                    seconds. The application hands control back to cvp_ccb_vxml.tcl with the
                                    parameter
                                    wait=X. |
|---|

| Name
                                             (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Wait Time | integer | Yes | true | false | None | Amount of time in seconds to wait. Maximum is 60,
                                          minimum is 0. |

| Name | Notes |
|---|---|
| done | The element is successfully run and the value is retrieved. |
| error | The element failed to
                                          retrieve the
                                          value. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Cisco > Callback | com.cisco.cvp.vxml.custelem.callback.Wait |

| Name (Label) | Notes |
|---|---|
| Event Type | You can select Java Exception , VXML Event , or Hotlink as event handler for this element. |