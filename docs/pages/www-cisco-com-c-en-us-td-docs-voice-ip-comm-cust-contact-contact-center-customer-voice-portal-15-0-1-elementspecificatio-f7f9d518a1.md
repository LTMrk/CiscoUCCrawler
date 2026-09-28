---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-15-0-1-elementspecificatio-f7f9d518a1
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/15-0-1/elementspecification/guide/ccvp_b_150-element-specifications-guide-for-cvp-vxml-and-call-studio/counter.html
retrieved_at: 2026-08-21T17:09:40.002545+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 15.0(1)

Updated: April 30, 2025

Chapter: Counter

## Chapter: Counter

# Counter

The Counter action element is used to keep track of a count stored as element data. The
                                    initial value of the count is defined as a configuration setting. In addition,
                                    the element may be configured to increment or decrement with a user defined
                                    step size. A typical use for the Counter element would be in a loop in the call
                                    flow that increments the count until a decision element decides that the loop
                                    must end. Revisiting a Counter element instance will automatically update the
                                    count.

## Settings

Name
                                             (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

initial

(Initial Count)

int

Yes

true

true

None

This
                                          setting specifies at which integer value this counter should
                                          start.

type

(Type)

string enum

Yes

true

true

None

This
                                          setting specifies whether the counter should be incremented or decremented.
                                          Possible values are: decrement | increment .

step

(Step Size)

int

Yes

true

true

1

This setting specifies by how
                                          much this counter should be incremented or
                                          decremented.

## Element Data

Name

Type

Notes

count

string

The current
                                          count

## Exit States

Name

Notes

done

The
                                          counter was
                                          updated.

## Folder and Class Information

Studio
                                             Element Folder Name

Class Name

Calculation

com.audium.server.action.counter.CounterAction

## Events

Name (Label)

Notes

Event Type

You can
                                          				  select Java Exception as event handler type.

The output of the Customer_Lookup element can be in JSON format . To know more about parsing the JSON Data refer to "Parsing
                              JSON Data" section in User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio.

| The Counter action element is used to keep track of a count stored as element data. The
                                    initial value of the count is defined as a configuration setting. In addition,
                                    the element may be configured to increment or decrement with a user defined
                                    step size. A typical use for the Counter element would be in a loop in the call
                                    flow that increments the count until a decision element decides that the loop
                                    must end. Revisiting a Counter element instance will automatically update the
                                    count. |
|---|

| Name
                                             (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| initial (Initial Count) | int | Yes | true | true | None | This
                                          setting specifies at which integer value this counter should
                                          start. |
| type (Type) | string enum | Yes | true | true | None | This
                                          setting specifies whether the counter should be incremented or decremented.
                                          Possible values are: decrement \| increment . |
| step (Step Size) | int | Yes | true | true | 1 | This setting specifies by how
                                          much this counter should be incremented or
                                          decremented. |

| Name | Type | Notes |
|---|---|---|
| count | string | The current
                                          count |

| Name | Notes |
|---|---|
| done | The
                                          counter was
                                          updated. |

| Studio
                                             Element Folder Name | Class Name |
|---|---|
| Calculation | com.audium.server.action.counter.CounterAction |

| Name (Label) | Notes |
|---|---|
| Event Type | You can
                                          				  select Java Exception as event handler type. |