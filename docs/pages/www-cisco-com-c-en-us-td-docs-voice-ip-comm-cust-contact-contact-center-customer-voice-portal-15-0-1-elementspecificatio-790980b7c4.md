---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-elementspecificatio-790980b7c4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/elementspecification/guide/ccvp_b_150-element-specifications-guide-for-cvp-vxml-and-call-studio/callback_disconnect_caller.html
retrieved_at: 2026-08-21T17:09:48.563413+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

Updated: April 30, 2025

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