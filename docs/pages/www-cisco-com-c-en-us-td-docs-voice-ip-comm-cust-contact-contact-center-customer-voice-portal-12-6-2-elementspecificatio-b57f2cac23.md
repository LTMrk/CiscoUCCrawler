---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-elementspecificatio-b57f2cac23
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/elementspecification/guide/ccvp_b_1262-element-specifications-guide/ccvp_mp_p2904c59_00_pod_read.html
retrieved_at: 2026-08-21T17:20:08.610293+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

Updated: April 28, 2023

Chapter: POD_Read

## Chapter: POD_Read

# POD_Read

Use the POD_Read element to read PODs that were created for a
                        		customer.

## Settings

Name (Label)

Type

Req'd

Single Setting Value

Substitution Allowed

Default

Notes

ID Type

String

Yes

True

False

Customer

This is a mandatory field.

User can select the type of id that is used for searching the POD.

ID

String

Yes

True

True

None

This is a mandatory field.

User can specify the ID to search the POD with.

## Element
                        	 Data

Name

Type

Notes

context_notes

string

Contains the Context_Notes data element associated with the POD.

context_pod_activity_link

string

Contains the Context_POD_Activity_Link data element associated
                                          						with the POD.

context_pod_source_cust_name

string

Contains the Context_POD_Source_Cust_Name data element
                                          						associated with the POD.

context_pod_source_email

string

Contains the Context_POD_Source_Email data element associated
                                          						with the POD.

context_pod_source_phone

string

Contains the Context_POD_Source_Phone data element associated
                                          						with the POD.

media_type

string

Contains the mediaType associated with the POD.

pod_id

string

In case
                                          						of a POD_Read by Customer ID, there might be multiple PODs matching the search
                                          						criteria. In that case, this contains the POD ID of the last updated POD.

search_result_as_json

string

Contains
                                          						details of all the PODs that match the search criteria in JSON format.

state

string

Contains the state of the POD.

tags

string

Contains the tags associated with the POD. Multiple tags are
                                          						separated by spaces.

## Exit
                        	 States

Name

Notes

done

The element is successfully run and the read POD operation is successful.

## Events

Name (Label)

Notes

Event Type

You can
                                          				  select Java Exception as event handler type.

The output of the Customer_Lookup element can be in JSON format . To know more about parsing the JSON Data refer to "Parsing
                              JSON Data" section in User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio.

| Name (Label) | Type | Req'd | Single Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| ID Type | String | Yes | True | False | Customer | This is a mandatory field. User can select the type of id that is used for searching the POD. |
| ID | String | Yes | True | True | None | This is a mandatory field. User can specify the ID to search the POD with. |

| Name | Type | Notes |
|---|---|---|
| context_notes | string | Contains the Context_Notes data element associated with the POD. |
| context_pod_activity_link | string | Contains the Context_POD_Activity_Link data element associated
                                          						with the POD. |
| context_pod_source_cust_name | string | Contains the Context_POD_Source_Cust_Name data element
                                          						associated with the POD. |
| context_pod_source_email | string | Contains the Context_POD_Source_Email data element associated
                                          						with the POD. |
| context_pod_source_phone | string | Contains the Context_POD_Source_Phone data element associated
                                          						with the POD. |
| media_type | string | Contains the mediaType associated with the POD. |
| pod_id | string | In case
                                          						of a POD_Read by Customer ID, there might be multiple PODs matching the search
                                          						criteria. In that case, this contains the POD ID of the last updated POD. |
| search_result_as_json | string | Contains
                                          						details of all the PODs that match the search criteria in JSON format. |
| state | string | Contains the state of the POD. |
| tags | string | Contains the tags associated with the POD. Multiple tags are
                                          						separated by spaces. |

| Name | Notes |
|---|---|
| done | The element is successfully run and the read POD operation is successful. |

| Name (Label) | Notes |
|---|---|
| Event Type | You can
                                          				  select Java Exception as event handler type. |