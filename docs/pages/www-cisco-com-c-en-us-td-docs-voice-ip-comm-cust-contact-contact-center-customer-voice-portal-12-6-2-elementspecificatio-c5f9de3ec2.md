---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cust-contact-contact-center-customer-voice-portal-12-6-2-elementspecificatio-c5f9de3ec2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/12-6-2/elementspecification/guide/ccvp_b_1262-element-specifications-guide/ccvp_mp_p0ca97e3_00_pod_add.html
retrieved_at: 2026-08-21T17:20:04.224298+00:00
---

Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

# Element Specifications for Cisco Unified CVP VXML Server and Call Studio, Release 12.6(2)

Updated: April 28, 2023

Chapter: POD_Add

## Chapter: POD_Add

# POD_Add

If the POD_Add element is run successfully, the customer's phone number is automatically populated in the Context_POD_Source_Phone data
                                                   element.

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

Customer ID

string

No

true

true

None

The
                                          						customer identification number.

Tags

string

No

true

true

None

A
                                          						comma-separated list of tags to be associated with the POD.

Field
                                          						Sets

string

Yes

true

true

None

A
                                          						comma-separated list of fieldsets. A fieldset is a grouping of related data
                                          						elements.

<DATA_ELEMENT>

string

No

false

true

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

Contains the unique ID for the POD that was created.

## Session
                        	 Data

Name

Type

Notes

PodId

string

Contains the
                                          				  unique ID for the POD if the POD creation is successful.

When a
                                          				  subdialog returns, IVR subsystem populates the POD.ID ECC variable with PodId . The Call Server sends the POD.ID ECC variable to Unified ICM.

## Exit
                        	 States

Name

Notes

done

The custom action element is added.

## Events

Name (Label)

Notes

Event Type

You can
                                          				  select Java Exception as event handler type.

The output of the Customer_Lookup element can be in JSON format . To know more about parsing the JSON Data refer to "Parsing
                              JSON Data" section in User Guide for Cisco Unified CVP VXML Server and Cisco Unified Call Studio.

| Use the POD_Add custom action element to create Piece of Data
                                    				(POD). You can associate the POD with a customer by using the Customer ID
                                    				field. The contributor of the POD is the VXML Server hostname. Note If the POD_Add element is run successfully, the customer's phone number is automatically populated in the Context_POD_Source_Phone data
                                                   element. | Note | If the POD_Add element is run successfully, the customer's phone number is automatically populated in the Context_POD_Source_Phone data
                                                   element. |
|---|---|---|
| Note | If the POD_Add element is run successfully, the customer's phone number is automatically populated in the Context_POD_Source_Phone data
                                                   element. |

| Note | If the POD_Add element is run successfully, the customer's phone number is automatically populated in the Context_POD_Source_Phone data
                                                   element. |
|---|---|

| Name
                                          						(Label) | Type | Req'd | Single
                                          						Setting Value | Substitution Allowed | Default | Notes |
|---|---|---|---|---|---|---|
| Customer ID | string | No | true | true | None | The
                                          						customer identification number. |
| Tags | string | No | true | true | None | A
                                          						comma-separated list of tags to be associated with the POD. |
| Field
                                          						Sets | string | Yes | true | true | None | A
                                          						comma-separated list of fieldsets. A fieldset is a grouping of related data
                                          						elements. |
| <DATA_ELEMENT> | string | No | false | true | None | User-defined data element that contains data about a POD. To add
                                          						additional data elements. perform the following steps: Right-click Field Sets setting name or the area below. Choose Add Data Element . You can
                                          						add, delete, or update the data elements by using these options: Add Data
                                                      								Element Delete Data
                                                      								Element Update Name |

| Name | Type | Notes |
|---|---|---|
| pod_id | string | Contains the unique ID for the POD that was created. |

| Name | Type | Notes |
|---|---|---|
| PodId | string | Contains the
                                          				  unique ID for the POD if the POD creation is successful. When a
                                          				  subdialog returns, IVR subsystem populates the POD.ID ECC variable with PodId . The Call Server sends the POD.ID ECC variable to Unified ICM. |

| Name | Notes |
|---|---|
| done | The custom action element is added. |

| Name (Label) | Notes |
|---|---|
| Event Type | You can
                                          				  select Java Exception as event handler type. |