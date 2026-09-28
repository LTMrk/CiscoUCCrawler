---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-aft-1-1-english-bell-canada-user-guide-user-can-bc-html-17b95c3d6b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/aft/1_1/english/bell_canada/user/guide/user_can/BC.html
retrieved_at: 2026-08-21T15:50:38.295238+00:00
---

ALI Formatting Tool User Guide for Bell Canada

# ALI Formatting Tool User Guide for Bell Canada

Updated: November 2, 2007

Chapter: Using the ALI Formatting Tool for Bell Canada

## Chapter: Using the ALI Formatting Tool for Bell Canada

## Using the ALI Formatting Tool for Bell Canada

This chapter provides information about the ALI Formatting Tool (AFT) fields that are specific to Bell Canada. Use this information along with "Using the ALI Formatting Tool" to generate ALI files in the format specified in Bell Canada's ALI data support documentation.

This chapter contains the following sections:

• NENA Fields and Corresponding Bell Canada Fields

• Modifying Bell Canada-Specific Fields in the ALI Formatting Tool

For more details, refer to the latest Bell Canada's ALI data support documentation.

## NENA Fields and Corresponding Bell Canada Fields

Table A-1 lists NENA fields and the corresponding Bell Canada fields. Be aware that some NENA fields and some Bell Canada fields must be populated with data and some may be left blank. For more details, refer to Bell Canada's ALI data support documentation.

For information about the Bell Canada-specific fields that you may need to modify, see the "Modifying Bell Canada-Specific Fields in the ALI Formatting Tool" section .

Table A-1 NENA Fields and Corresponding Bell Canada Fields

House Number

Yes

Civic Number

Yes

House Number Suffix

No

Civic Number Suffix

No

Street Name

Yes

Street Name

Yes

Prefix Directional

No

Street Directional

No

Street Suffix

No

Street Suffix

Yes

The Street Suffix field is not mandatory in NENA but must be data filled in the Bell Canada format.

Post Directional

No

Not applicable

This NENA field is not used by Bell Canada.

Community Name

Yes

Extended Municipality Name

Yes

State

Yes

Province

Yes

Main NPA

No

Pilot NPA

Yes

Main Telephone No.

No

Pilot NXX + Pilot LINE

Yes

Customer Name

Yes

Subscriber Name

Yes

Class of Service

Yes

Not applicable

AFT does not use the Class of Service from Cisco Emergency Responder (Cisco ER). You must configure this in AFT. See Table A-3 .

However, you must enter a dummy value (1 alphanumeric character) for this mandatory field in Cisco ER for the Cisco ER ALI configuration to work correctly.

Type of Service

Yes

Not applicable

Because this is a mandatory field in NENA, you must configure some dummy value for this field in Cisco ER.

AFT ignores this value.

Exchange

No

Not applicable

This NENA field is not used by Bell Canada.

Order Number

No

Not applicable

This NENA field is not used by Bell Canada.

Extract Date

No

Not applicable

This NENA field is not used by Bell Canada.

County

No

Not applicable

This NENA field is not used by Bell Canada.

Company ID

Yes

DATA LSP ID

Yes

Zip Code

No

Not applicable

This NENA field is not used by Bell Canada.

Postal Code is defined in a Bell Canada-specific field. See Table A-3 .

Zip Code Extension

No

Not applicable

This NENA field is not used by Bell Canada.

Customer Code

Yes

Subscriber Account ID

Yes

Comments

No

Not applicable

This NENA field is not used by Bell Canada.

Longitude

No

Not applicable

This NENA field is not used by Bell Canada.

Latitude

No

Not applicable

This NENA field is not used by Bell Canada.

Elevation

No

Not applicable

This NENA field is not used by Bell Canada.

TAR code

No

Not applicable

This NENA field is not used by Bell Canada.

Location

No

Additional Information

No

Reserved (for Service Provider Use)

No

Not applicable

This NENA field is not used by Bell Canada.

Note The NENA Function Code field is called Transaction Code field in the Bell Canada format. See the "Modifying the Transaction Code" section .

## Modifying Bell Canada-Specific Fields in the ALI Formatting Tool

This section covers the following topics:

• Modifying the Transaction Code

• Entering Bell Canada-Specific Data

### Modifying the Transaction Code

Table A-2 shows the values displayed in the Function Field in NENA records and the corresponding values for the Transaction Code in Bell Canada records.

.

Table A-2 NENA and Bell Canada Function/Transaction Fields

I for Insert a new record

A for Add a new record

C for Change a record

A for Change a record.

The NENA Function Code C is mapped to Bell Canada's Transaction Code A.

D for Delete a record

D for Delete a record

Make sure that the Transaction Code for Bell Canada is either A or D. Otherwise, Bell Canada will reject the record and return the record in an Error Return file with an error message.

### Entering Bell Canada-Specific Data

Table A-3 describes the remaining Bell Canada-specific fields. Some require data to generate ALI files in the format specified in Bell Canada's ALI data support documentation; others may remain blank.

If there is an error in these fields, Bell Canada will reject the record and send back a Error Return file with an error code. For more details and for information about field validation, refer to the latest Bell Canada ALI data support documentation.

Table A-3 Modifying Bell Canada Specific-Fields

Service Class

Type of telephone service of the customer's Terminal Number

3 alphanumeric characters

Must not be blank.

Postal Code

Postal code of the customer's service address

6 alphanumeric characters

Must not be blank.

First character must be alphabetic.

Municipality Code

Unique code assigned to each municipality

3 alphanumeric characters

Must not be blank.

Class of Service

Code identify the grade, class and type of service

5 alphanumeric characters

May be blank.

System Source

Identifies the source database of the Transaction Record

1 alphabetic character

Must not be blank.

Location Type

Type of location within a building (for example, apartment)

15 alphanumeric characters

May be blank.

Location Number

Number of the location identified in the Location Type field (for example, apartment 2, floor 2)

6 alphanumeric characters

May be blank.

Service Municipality

City, town, village, borough or locality

35 alphanumeric characters

Must not be blank.

LSP ID

Unique code provided to the PS ALI customer by Bell Canada. It denotes the provider of local telephone service.

5 alphanumeric characters

Must not be blank.

Must be the valid LSP Identifier provided to the PS ALI customer.

Note You do not configure the Language Indicator field using AFT; AFT sets the field to E for English.

| NENA Fields | Data Required | Bell Canada Fields | Data Required | Comments |
|---|---|---|---|---|
| House Number | Yes | Civic Number | Yes |  |
| House Number Suffix | No | Civic Number Suffix | No |  |
| Street Name | Yes | Street Name | Yes |  |
| Prefix Directional | No | Street Directional | No |  |
| Street Suffix | No | Street Suffix | Yes | The Street Suffix field is not mandatory in NENA but must be data filled in the Bell Canada format. |
| Post Directional | No |  | Not applicable | This NENA field is not used by Bell Canada. |
| Community Name | Yes | Extended Municipality Name | Yes |  |
| State | Yes | Province | Yes |  |
| Main NPA | No | Pilot NPA | Yes |  |
| Main Telephone No. | No | Pilot NXX + Pilot LINE | Yes |  |
| Customer Name | Yes | Subscriber Name | Yes |  |
| Class of Service | Yes |  | Not applicable | AFT does not use the Class of Service from Cisco Emergency Responder (Cisco ER). You must configure this in AFT. See Table A-3 . However, you must enter a dummy value (1 alphanumeric character) for this mandatory field in Cisco ER for the Cisco ER ALI configuration to work correctly. |
| Type of Service | Yes |  | Not applicable | Because this is a mandatory field in NENA, you must configure some dummy value for this field in Cisco ER. AFT ignores this value. |
| Exchange | No |  | Not applicable | This NENA field is not used by Bell Canada. |
| Order Number | No |  | Not applicable | This NENA field is not used by Bell Canada. |
| Extract Date | No |  | Not applicable | This NENA field is not used by Bell Canada. |
| County | No |  | Not applicable | This NENA field is not used by Bell Canada. |
| Company ID | Yes | DATA LSP ID | Yes |  |
| Zip Code | No |  | Not applicable | This NENA field is not used by Bell Canada. Postal Code is defined in a Bell Canada-specific field. See Table A-3 . |
| Zip Code Extension | No |  | Not applicable | This NENA field is not used by Bell Canada. |
| Customer Code | Yes | Subscriber Account ID | Yes |  |
| Comments | No |  | Not applicable | This NENA field is not used by Bell Canada. |
| Longitude | No |  | Not applicable | This NENA field is not used by Bell Canada. |
| Latitude | No |  | Not applicable | This NENA field is not used by Bell Canada. |
| Elevation | No |  | Not applicable | This NENA field is not used by Bell Canada. |
| TAR code | No |  | Not applicable | This NENA field is not used by Bell Canada. |
| Location | No | Additional Information | No |  |
| Reserved (for Service Provider Use) | No |  | Not applicable | This NENA field is not used by Bell Canada. |

| NENA Function Code Field | Bell Canada Transaction Code Field |
|---|---|
| I for Insert a new record | A for Add a new record |
| C for Change a record | A for Change a record. The NENA Function Code C is mapped to Bell Canada's Transaction Code A. |
| D for Delete a record | D for Delete a record |

| Field | Description | Format | Notes |
|---|---|---|---|
| Service Class | Type of telephone service of the customer's Terminal Number | 3 alphanumeric characters | Must not be blank. |
| Postal Code | Postal code of the customer's service address | 6 alphanumeric characters | Must not be blank. First character must be alphabetic. |
| Municipality Code | Unique code assigned to each municipality | 3 alphanumeric characters | Must not be blank. |
| Class of Service | Code identify the grade, class and type of service | 5 alphanumeric characters | May be blank. |
| System Source | Identifies the source database of the Transaction Record | 1 alphabetic character | Must not be blank. |
| Location Type | Type of location within a building (for example, apartment) | 15 alphanumeric characters | May be blank. |
| Location Number | Number of the location identified in the Location Type field (for example, apartment 2, floor 2) | 6 alphanumeric characters | May be blank. |
| Service Municipality | City, town, village, borough or locality | 35 alphanumeric characters | Must not be blank. |
| LSP ID | Unique code provided to the PS ALI customer by Bell Canada. It denotes the provider of local telephone service. | 5 alphanumeric characters | Must not be blank. Must be the valid LSP Identifier provided to the PS ALI customer. |