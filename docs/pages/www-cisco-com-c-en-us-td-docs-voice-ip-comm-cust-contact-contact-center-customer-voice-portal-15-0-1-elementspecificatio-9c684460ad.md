---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-elementspecificatio-9c684460ad
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/elementspecification/guide/ccvp_b_150-element-specifications-guide-for-cvp-vxml-and-call-studio/callback_get_status.html
retrieved_at: 2026-08-21T17:09:57.166904+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

Updated: April 30, 2025

Chapter: Callback_Get_Status

## Chapter: Callback_Get_Status

# Callback_Get_Status

The Callback_Get_Status element is responsible for
                                    retrieving all information about the callback related to the current call (if a
                                    callback
                                    exists).

## Settings

None.

## Element Data

Name

Type

Notes

startCallback

boolean

Specifies whether the
                                          application should call the caller, given current caller position in queue and
                                          rate of de-queue.

ewt

int

Current estimated remaining wait time in seconds
                                          for this caller before the callback should be initiated.

qpos

int

Current position in
                                          queue.

rec

string

Recording URL that was stored in the callback table. This only needs to
                                          be returned if startCallback is true.

DORateA

int

Average number of seconds
                                          that it takes for each caller in this queue to leave the queue. This includes
                                          both callers leaving queue by going to agents and callers in queue
                                          abandoning.

DORateB

int

Average number of seconds that it takes for the #1
                                          caller in this queue to leave the queue.

RORate

int

Average number of seconds
                                          that it takes to get the caller back after starting the callback. The rate is
                                          the same for all queues. This includes dial time, ring time, and IVR time spent
                                          asking the caller if they are ready to take the callback.

cli

string

The Calling Line ID to
                                          be used for this callback

rna

int

Ring No Answer timeout for this
                                          call

dn

string

Destination number for this outbound
                                          call

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

com.cisco.cvp.vxml.custelem.callback.GetStatus

## Events

Name (Label)

Notes

Event Type

You can
                                          				  select Java Exception as event handler type.

The output of the Customer_Lookup element can be in JSON format . To know more about parsing the JSON Data refer to "Parsing
                              JSON Data" section in User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio.

| The Callback_Get_Status element is responsible for
                                    retrieving all information about the callback related to the current call (if a
                                    callback
                                    exists). |
|---|

| Name | Type | Notes |
|---|---|---|
| startCallback | boolean | Specifies whether the
                                          application should call the caller, given current caller position in queue and
                                          rate of de-queue. |
| ewt | int | Current estimated remaining wait time in seconds
                                          for this caller before the callback should be initiated. |
| qpos | int | Current position in
                                          queue. |
| rec | string | Recording URL that was stored in the callback table. This only needs to
                                          be returned if startCallback is true. |
| DORateA | int | Average number of seconds
                                          that it takes for each caller in this queue to leave the queue. This includes
                                          both callers leaving queue by going to agents and callers in queue
                                          abandoning. |
| DORateB | int | Average number of seconds that it takes for the #1
                                          caller in this queue to leave the queue. |
| RORate | int | Average number of seconds
                                          that it takes to get the caller back after starting the callback. The rate is
                                          the same for all queues. This includes dial time, ring time, and IVR time spent
                                          asking the caller if they are ready to take the callback. |
| cli | string | The Calling Line ID to
                                          be used for this callback |
| rna | int | Ring No Answer timeout for this
                                          call |
| dn | string | Destination number for this outbound
                                          call |

| Name | Notes |
|---|---|
| done | The element is successfully run and the value is retrieved. |
| error | The element failed to
                                          retrieve the
                                          value. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Cisco > Callback | com.cisco.cvp.vxml.custelem.callback.GetStatus |

| Name (Label) | Notes |
|---|---|
| Event Type | You can
                                          				  select Java Exception as event handler type. |