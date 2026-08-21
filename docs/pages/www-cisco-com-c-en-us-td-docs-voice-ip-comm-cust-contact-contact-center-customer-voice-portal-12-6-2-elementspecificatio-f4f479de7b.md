---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-elementspecificatio-f4f479de7b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/elementspecification/guide/ccvp_b_1262-element-specifications-guide/ccvp_mp_cf36b584_00_callback_disconnect_caller.html
retrieved_at: 2026-08-21T17:15:27.779025+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

Updated: April 28, 2023

Chapter: Callback_Disconnect_Caller

## Chapter: Callback_Disconnect_Caller

# Callback_Disconnect_Caller

The Callback_Disconnect_Caller element is responsible
                                    for disconnecting the caller’s leg of the call. The IP leg of the call for
                                    Unified CVP is preserved to hold the caller’s place in
                                       line until the callback is made back to the caller.

## Settings

Name
                                             (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

Probe Type

string enum

Yes

Yes

No

Disconnect
                                          Caller

The probe type can be one of: Disconnect Caller | Intercept Caller
                                             Hangup | No Intercept Caller
                                             Hangup

## Element Data

Name

Type

Notes

Result

string

The call outcome from the attempt to disconnect
                                          the caller’s
                                          leg.

## Exit States

Name

Notes

done

The element is successfully run to retrieve the value.

error

The element failed to
                                          retrieve the
                                          value.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Cisco > Callback

com.cisco.cvp.vxml.custelem.callback.DisconnectCaller

## Events

Name (Label)

Notes

Event Type

You can select Java Exception , VXML Event , or Hotlink as event handler for this element.

| The Callback_Disconnect_Caller element is responsible
                                    for disconnecting the caller’s leg of the call. The IP leg of the call for
                                    Unified CVP is preserved to hold the caller’s place in
                                       line until the callback is made back to the caller. |
|---|

| Name
                                             (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Probe Type | string enum | Yes | Yes | No | Disconnect
                                          Caller | The probe type can be one of: Disconnect Caller \| Intercept Caller
                                             Hangup \| No Intercept Caller
                                             Hangup |

| Name | Type | Notes |
|---|---|---|
| Result | string | The call outcome from the attempt to disconnect
                                          the caller’s
                                          leg. |

| Name | Notes |
|---|---|
| done | The element is successfully run to retrieve the value. |
| error | The element failed to
                                          retrieve the
                                          value. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Cisco > Callback | com.cisco.cvp.vxml.custelem.callback.DisconnectCaller |

| Name (Label) | Notes |
|---|---|
| Event Type | You can select Java Exception , VXML Event , or Hotlink as event handler for this element. |