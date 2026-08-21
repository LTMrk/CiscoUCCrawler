---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-elementspecificat-96f1a6f998
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/elementspecification/guide/ccvp_b_1261-element-specifications-guide/ccvp_mp_c47a834a_00_callback_reconnect.html
retrieved_at: 2026-08-21T17:23:45.285306+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

Updated: February 18, 2020

Chapter: Callback_Reconnect

## Chapter: Callback_Reconnect

# Callback_Reconnect

The Callback_Reconnect element is responsible for reconnecting the caller’s leg of the
                                    call.

## Settings

Name
                                             (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

Dialed Number

string

Yes

true

true

None

Destination for the outbound
                                          call.

Calling Line
                                          ID

string

Yes

true

true

None

The
                                          calling line ID to be used for the callback.

Ring No Answer Timeout

string

Yes

true

true

30

Ring No Answer timeout in
                                          seconds, The default is 30, minimum is 0 and maximum is 300
                                          seconds.

User-to-User
                                          Information

string

No

true

true

None

The
                                          user-to-user information (UUI) to include in the
                                          callback.

## Element Data

Name

Type

Notes

result

string

Contains the reconnect exit
                                          state.

## Exit States

Name

Notes

noanswer

The callback was attempted and not answered.

busy

The
                                          callback was attempted and the calling line was busy.

invalid_number

The callback number was not a valid number.

connected

The callback was attempted and connected.

error

The
                                          element failed to retrieve the
                                          value.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Cisco > Callback

com.cisco.cvp.vxml.custelem.callback.Reconnect

## Events

Name (Label)

Notes

Event Type

You can select Java Exception , VXML Event , or Hotlink as event handler for this element.

| The Callback_Reconnect element is responsible for reconnecting the caller’s leg of the
                                    call. |
|---|

| Name
                                             (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Dialed Number | string | Yes | true | true | None | Destination for the outbound
                                          call. |
| Calling Line
                                          ID | string | Yes | true | true | None | The
                                          calling line ID to be used for the callback. |
| Ring No Answer Timeout | string | Yes | true | true | 30 | Ring No Answer timeout in
                                          seconds, The default is 30, minimum is 0 and maximum is 300
                                          seconds. |
| User-to-User
                                          Information | string | No | true | true | None | The
                                          user-to-user information (UUI) to include in the
                                          callback. |

| Name | Type | Notes |
|---|---|---|
| result | string | Contains the reconnect exit
                                          state. |

| Name | Notes |
|---|---|
| noanswer | The callback was attempted and not answered. |
| busy | The
                                          callback was attempted and the calling line was busy. |
| invalid_number | The callback number was not a valid number. |
| connected | The callback was attempted and connected. |
| error | The
                                          element failed to retrieve the
                                          value. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Cisco > Callback | com.cisco.cvp.vxml.custelem.callback.Reconnect |

| Name (Label) | Notes |
|---|---|
| Event Type | You can select Java Exception , VXML Event , or Hotlink as event handler for this element. |