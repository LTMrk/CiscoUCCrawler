---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-6-elementspecificat-83746c344d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_6/elementspecification/guide/ccvp_b_1261-element-specifications-guide/ccvp_mp_c0798d96_00_callback_validate.html
retrieved_at: 2026-08-21T17:23:57.973580+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(1)

Updated: February 18, 2020

Chapter: Callback_Validate

## Chapter: Callback_Validate

# Callback_Validate

The Callback_Validate element is responsible for verifying whether or not a callback can be offered
                                    to the caller during this call. Depending on the outcome of the validation, the
                                    Validate element exits with one of four
                                    states.

## Settings

None.

## Element Data

Name

Type

Notes

result

string

Contains the exit
                                          state result.

ewt

int

EWT value passed from Unified
                                          ICM.

gw

string

Gateway identifier.

loc

string

Gateway location information.

capacity

int

Gateway
                                          capacity.

## Exit States

Name

Notes

preemptive

This callback is valid.

none

The callback is not
                                          allowed.

refresh

The validation could
                                          not be performed because the DBServlet needs a reference data refresh. The
                                          application must call SetQueueDefaults before validation can
                                          occur.

error

The element failed to
                                          retrieve the
                                          value.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Cisco > Callback

com.cisco.cvp.vxml.custelem.callback.Validate

## Events

Name (Label)

Notes

Event Type

You can select Java Exception , VXML Event , or Hotlink as event handler for this element.

| The Callback_Validate element is responsible for verifying whether or not a callback can be offered
                                    to the caller during this call. Depending on the outcome of the validation, the
                                    Validate element exits with one of four
                                    states. |
|---|

| Name | Type | Notes |
|---|---|---|
| result | string | Contains the exit
                                          state result. |
| ewt | int | EWT value passed from Unified
                                          ICM. |
| gw | string | Gateway identifier. |
| loc | string | Gateway location information. |
| capacity | int | Gateway
                                          capacity. |

| Name | Notes |
|---|---|
| preemptive | This callback is valid. |
| none | The callback is not
                                          allowed. |
| refresh | The validation could
                                          not be performed because the DBServlet needs a reference data refresh. The
                                          application must call SetQueueDefaults before validation can
                                          occur. |
| error | The element failed to
                                          retrieve the
                                          value. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Cisco > Callback | com.cisco.cvp.vxml.custelem.callback.Validate |

| Name (Label) | Notes |
|---|---|
| Event Type | You can select Java Exception , VXML Event , or Hotlink as event handler for this element. |