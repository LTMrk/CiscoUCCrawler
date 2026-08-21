---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-elementspecificatio-4881d95f07
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/elementspecification/guide/ccvp_b_150-element-specifications-guide-for-cvp-vxml-and-call-studio/callback_updated_status.html
retrieved_at: 2026-08-21T17:10:09.854020+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

Updated: April 30, 2025

Chapter: Callback_Update_Status

## Chapter: Callback_Update_Status

# Callback_Update_Status

The Callback_Update_Status element is responsible for
                                    updating the database after a callback disconnect or
                                    reconnect.

## Settings

Name
                                             (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

status

enum string

Yes

true

true

None

Callback status can be one of the
                                          following:

PENDING

INPROGRESS

COMPLETED

ADD TO
                                                QUEUE

DROP FROM QUEUE

reason

enum string

*

true

true

None

Required if status is COMPLETED, one of the
                                          following:

error

busy

noanswer

noresponse

invalid_number

connected

trunkbusy

caller_cancelled

## Element Data

Name

Type

Notes

result

string

Tells the application whether to
                                          cancel the existing callback or to retry, can be one of the
                                          following:

cancel

retry

done

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

com.cisco.cvp.vxml.custelem.callback.UpdateStatus

## Events

Name (Label)

Notes

Event Type

You can
                                          				  select Java Exception as event handler type.

The output of the Customer_Lookup element can be in JSON format . To know more about parsing the JSON Data refer to "Parsing
                              JSON Data" section in User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio.

| The Callback_Update_Status element is responsible for
                                    updating the database after a callback disconnect or
                                    reconnect. |
|---|

| Name
                                             (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| status | enum string | Yes | true | true | None | Callback status can be one of the
                                          following: PENDING INPROGRESS COMPLETED ADD TO
                                                QUEUE DROP FROM QUEUE |
| reason | enum string | * | true | true | None | Required if status is COMPLETED, one of the
                                          following: error busy noanswer noresponse invalid_number connected trunkbusy caller_cancelled |

| Name | Type | Notes |
|---|---|---|
| result | string | Tells the application whether to
                                          cancel the existing callback or to retry, can be one of the
                                          following: cancel retry done |

| Name | Notes |
|---|---|
| done | The element is successfully run and the value is retrieved. |
| error | The element failed to
                                          retrieve the
                                          value. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Cisco > Callback | com.cisco.cvp.vxml.custelem.callback.UpdateStatus |

| Name (Label) | Notes |
|---|---|
| Event Type | You can
                                          				  select Java Exception as event handler type. |