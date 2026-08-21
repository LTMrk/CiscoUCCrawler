---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-elementspecificatio-e809b9272d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/elementspecification/guide/ccvp_b_1262-element-specifications-guide/ccvp_m_pod_update.html
retrieved_at: 2026-08-21T17:20:13.020866+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

Updated: April 28, 2023

Chapter: POD_Update

## Chapter: POD_Update

# POD_Update

Use the POD_Update custom action element to update a POD. You
                                    				can update a POD by providing the pod_id. The update contributor of the POD is
                                    				the VXML Server hostname.

If you update the tags, fieldsets, or user-defined data elements
                                    				with new values, the new values are appended.

## Settings

Name
                                          						(Label)

Type

Req'd

Single
                                          						Setting Value

Substitution Allowed

Default

Notes

POD ID

String

Yes

True

True

None

The
                                          						unique ID for the POD.

Customer
                                          						ID

String

No

True

True

None

An
                                          						optional setting, to update the Customer ID in the POD_Update element.

Tags

String

No

True

True

None

A
                                          						comma-separated list of tags to be associated with the POD.

Field
                                          						Sets

String

No

True

True

None

A
                                          						comma-separated list of fieldsets. A fieldset is a grouping of related data
                                          						elements.

<DATA_ELEMENT>

String

No

False

True

None

User-defined data element that contains data about a POD.

Right-click

Choose Add Data Element .

Add Data
                                                      								Element

Delete Data
                                                      								Element

Update Name

## Element
                        	 Data

Name

Type

Notes

pod_id

string

Contains
                                          				  the unique ID for the POD that was updated.

## Exit
                        	 States

Name

Notes

done

The custom action element is updated.

## Events

Name (Label)

Notes

Event Type

You can
                                          				  select Java Exception as event handler type.

The output of the Customer_Lookup element can be in JSON format . To know more about parsing the JSON Data refer to "Parsing
                              JSON Data" section in User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio.

| Use the POD_Update custom action element to update a POD. You
                                    				can update a POD by providing the pod_id. The update contributor of the POD is
                                    				the VXML Server hostname. If you update the tags, fieldsets, or user-defined data elements
                                    				with new values, the new values are appended. |
|---|

| Name
                                          						(Label) | Type | Req'd | Single
                                          						Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| POD ID | String | Yes | True | True | None | The
                                          						unique ID for the POD. |
| Customer
                                          						ID | String | No | True | True | None | An
                                          						optional setting, to update the Customer ID in the POD_Update element. |
| Tags | String | No | True | True | None | A
                                          						comma-separated list of tags to be associated with the POD. |
| Field
                                          						Sets | String | No | True | True | None | A
                                          						comma-separated list of fieldsets. A fieldset is a grouping of related data
                                          						elements. |
| <DATA_ELEMENT> | String | No | False | True | None | User-defined data element that contains data about a POD. To add
                                          						more data elements, perform the following steps: Right-click Field Sets setting name or the surrounding area. Choose Add Data Element . You
                                          						can add, delete, or update the data elements by using these options: Add Data
                                                      								Element Delete Data
                                                      								Element Update Name |

| Name | Type | Notes |
|---|---|---|
| pod_id | string | Contains
                                          				  the unique ID for the POD that was updated. |

| Name | Notes |
|---|---|
| done | The custom action element is updated. |

| Name (Label) | Notes |
|---|---|
| Event Type | You can
                                          				  select Java Exception as event handler type. |