---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-cvp-12-5-reference-guide-c-c31c0a3eab
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp_12_5/reference/guide/ccvp_b_1251-element-specification-guide-cvp/ccvp_mp_c7092e41_00_callback_enter_queue.html
retrieved_at: 2026-08-21T17:31:27.601326+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.5(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.5(1)

Updated: January 31, 2020

Chapter: Callback_Enter_Queue

## Chapter: Callback_Enter_Queue

# Callback_Enter_Queue

The Callback_Enter_Queue element is responsible for adding a new caller to the queue. This element must be run for all callers even if the caller
                                    may not be offered a callback.

## Settings

None.

## Element Data

Name

Type

Notes

ewt

int

The calculated estimated
                                          wait time for caller in
                                          queue.

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

com.cisco.cvp.vxml.custelem.callback.EnterQueue

## Events

Name (Label)

Notes

Event Type

You can
                                          				  select Java Exception as event handler type.

The output of the Customer_Lookup element can be in JSON format . To know more about parsing the JSON Data refer to "Parsing
                              JSON Data" section in User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio.

| The Callback_Enter_Queue element is responsible for adding a new caller to the queue. This element must be run for all callers even if the caller
                                    may not be offered a callback. |
|---|

| Name | Type | Notes |
|---|---|---|
| ewt | int | The calculated estimated
                                          wait time for caller in
                                          queue. |

| Name | Notes |
|---|---|
| done | The element is successfully run and the value is retrieved. |
| error | The element failed to
                                          retrieve the
                                          value. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Cisco > Callback | com.cisco.cvp.vxml.custelem.callback.EnterQueue |

| Name (Label) | Notes |
|---|---|
| Event Type | You can
                                          				  select Java Exception as event handler type. |