---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-12-5-1su4-english-administration-guide-cer0-b-cisco-emergency-responder--160f9b49b8
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/12_5_1su4/english/administration/guide/cer0_b_cisco-emergency-responder-administration-guide-1251su4/cer0_b_cisco-emergency-responder-administration-guide-1251su3_appendix_010101.html
retrieved_at: 2026-08-21T15:40:07.016445+00:00
---

Cisco Emergency Responder Administration Guide for Release 12.5(1)SU4

# Cisco Emergency Responder Administration Guide for Release 12.5(1)SU4

Updated: August 23, 2023

Chapter: Using AFT for Specific Service Providers

## Chapter: Using AFT for Specific Service Providers

# Using AFT for Specific Service Providers

## ALI Formatting Tool
                        	 for Bell Canada

The following
                           		topics describe how to use AFT for Bell Canada.

### Transaction Code
                           	 Modifications

When using
                                 		  the AFT with Bell Canada as your service provider, ensure that the Transaction
                                 		  Code for Bell Canada is either A or D. Otherwise, Bell Canada rejects the
                                 		  record and returns it in an Error Return file with an error message.

The
                                 		  following table shows the values displayed in the Function Field in NENA
                                 		  records and the corresponding values for the Transaction Code in Bell Canada
                                 		  records.

NENA Function Code Field

Bell Canada Transaction Code Field

I
                                             					 for Insert a new record.

A
                                             					 for Add a new record.

C
                                             					 for Change a record.

A
                                             					 for Change a record.

The NENA
                                                         						Function Code C is mapped to Bell Canada's Transaction Code A.

D
                                             					 for Delete a record.

D
                                             					 for Delete a record.

### Bell Canada Data

The
                                 		  following table describes the remaining Bell Canada-specific fields. Some
                                 		  fields require data to generate ALI files in the format specified in Bell
                                 		  Canada's ALI data support documentation; other fields can remain blank.

If there is
                                 		  an error in these fields, Bell Canada rejects the record and sends back an
                                 		  Error Return file with an error code.

You do not
                                             			 configure the Language Indicator field using AFT; AFT sets the field to E for
                                             			 English.

Field

Description

Format

Notes

Service Class

Type of telephone service of the customer's Terminal Number.

3
                                             					 alphanumeric characters

Required field.

Postal Code

Postal code of the customer's service address.

6
                                             					 alphanumeric characters

Required field. The first character must be alphabetic.

Municipality Code

Unique code assigned to each municipality.

3
                                             					 alphanumeric characters

Required field.

Class of Service

Code that identifies the grade, class, and type of service.

5
                                             					 alphanumeric characters

Required field.

System Source

Identifies the source database of the Transaction Record.

1
                                             					 alphabetic character

Required field.

Location Type

Type of location within a building (for example, apartment).

15
                                             					 alphanumeric characters

Optional field.

Location Number

Number of the location identified in the Location Type field
                                             					 (for example, apartment 2, floor 2).

6
                                             					 alphanumeric characters

Optional field.

Service Municipality

City, town, village, borough, or locality.

35
                                             					 alphanumeric characters

Required field.

LSP
                                             					 ID

Unique code provided to the PS ALI customer by Bell Canada that
                                             					 denotes the provider of local telephone service.

5
                                             					 alphanumeric characters

Required field.

Must be the valid LSP Identifier provided to the PS ALI customer
                                             					 by Bell Canada.

## ALI Formatting Tool
                        	 for SBC Ameritech

SBC Ameritech
                           		(Ameritech) does not have any service provider-specific fields that you must
                           		modify using the AFT. However, when using AFT to format records for Ameritech,
                           		you may need to modify the Function Code.

Cisco
                           		Emergency Responder (Emergency Responder) sets the Function Code to one of the
                           		following:

I for Inserting a
                                 			 new ALI record (the default)

C for Updating an
                                 			 ALI record, such as changing a street name

D for Deleting an
                                 			 ALI record

If you make
                           		changes to an ALI record in Emergency Responder to correct errors reported by
                           		Ameritech, you may need to use AFT to change the Function Code for ELIN
                           		records.

For example,
                           		Emergency Responder initially generates ALI records with a function code of I
                           		for Insert. After you format a file and export it to Ameritech using AFT,
                           		Ameritech may reject the file because of an error, such as the street suffix is
                           		incorrect. You cannot change the street suffix in AFT because this field is
                           		disabled. Instead, you must change the ALI record using Emergency Responder.

When
                           		Emergency Responder generates the ALI record the second time after you make the
                           		change, it sets the Function Code to C because it assumes that the first file
                           		was accepted. Use AFT to change the Function Code for ELIN records from C to I.
                           		Then, generate the format using AFT and send the reformatted file to Ameritech.

## ALI Formatting Tool for SBC-PacBell

The following sections describe how to use the AFT for SBC-PacBell.

### Call Back for ELIN
                           	 Enablement

Emergency
                              		Responder displays the ELIN at the PSAP. If the emergency call is cut off for
                              		any reason, or if the PSAP needs to talk to the caller again, the PSAP can then
                              		dial to reconnect to the emergency caller.

The call back
                              		for this ELIN option allows you to specify a direct inward dial (DID) number
                              		that can be used by the PSAP when a call from a fictitious number is made to
                              		911.

The call back
                              		for this ELIN option performs two important functions:

It alerts the PSAP
                                    			 that the phone they are calling back may not have generated the 911 call.

It enables the
                                    			 PSAP to call back to a phone that is located near the fictitious telephone
                                    			 number that did place the call.

We recommend
                              		that you always enable this option by checking the call back for this ELIN
                              		field. (The default is to leave the field blank, which defaults to No.)

### Function Code
                           	 Modifications

Emergency
                              		Responder sets the function code to one of the following:

I for Inserting a
                                    			 new ALI record (the default)

C for Updating an
                                    			 ALI record, such as changing a street name

D for Deleting an
                                    			 ALI record

If you make
                              		changes to an ALI record in Emergency Responder to correct errors reported by
                              		your service provider, you may need to use AFT to change the function code for
                              		ELIN records.

For example,
                              		Emergency Responder initially generates ALI records with a function code of I
                              		for Insert. After you format a file and export it to SBC Pacific Bell (PacBell)
                              		using AFT, PacBell may reject the file. The error may be that the street suffix
                              		is incorrect, for example. You cannot change the street suffix in AFT because
                              		this field is disabled. You must change the ALI record using Emergency
                              		Responder.

When
                              		Emergency Responder generates the ALI record the second time after you make the
                              		change, it sets the function code to C because it assumes that the first file
                              		was accepted. Use AFT to change the Function Code for ELIN records from C to I.
                              		Then, generate the format using AFT and send the reformatted file to PacBell.

## ALI Formatting Tool for SBC-Southwestern Bell

The following sections describe how to use the AFT for SBC-Southwestern Bell.

### PS Code for SBC-Southwestern Bell

To make the ELIN records readable by Southwestern Bell, you may need to use AFT to update the PS Code field; this field is
                              specific to Southwestern Bell. The PS Code is a four-digit code that the Southwestern Bell system assigns whenever the system
                              configures a new PS site. This code is associated with the PS user's login and source.

The PS Code is a feature that allows only records with the correct PS Code to be processed into tables for the PS Site. If
                              the PS Code does not match the configured Source Name that is assigned to the PS Site, the record will not process. Before
                              you generate a formatted file using AFT, make sure that PS Code and the Source Name match. For more information, see the Southwestern
                              Bell documentation.

### Function Code
                           	 Modifications

Emergency
                              		Responder sets the function code to one of the following:

I for Inserting a
                                    			 new ALI record (the default)

C for Updating an
                                    			 ALI record, such as changing a street name

D for Deleting an
                                    			 ALI record

If you make
                              		changes to an ALI record in Emergency Responder to correct errors reported by
                              		your service provider, you may need to use AFT to change the function code for
                              		ELIN records.

For example,
                              		Emergency Responder initially generates ALI records with a function code of I
                              		for Insert. After you format a file and export it to Southwestern Bell using
                              		AFT, Southwestern Bell may reject the file. The error may be that the street
                              		suffix is incorrect, for example. You cannot change the street suffix in AFT
                              		because this field is disabled. You must change the ALI record using Emergency
                              		Responder.

When
                              		Emergency Responder generates the ALI record the second time after you make the
                              		change, it sets the function code to C because it assumes that the first file
                              		was accepted. Use AFT to change the function code for ELIN records from C to I.
                              		Then, generate the format using AFT and send the reformatted file to
                              		Southwestern Bell.

## ALI Formatting Tool
                        	 for Qwest

Qwest does
                           		not have any service provider-specific fields that you must modify using the
                           		AFT. However, when using AFT to format records for Qwest, you may need to
                           		modify the function code.

Cisco
                           		Emergency Responder (Emergency Responder) sets the function code to one of the
                           		following:

I for Inserting a
                                 			 new ALI record (the default)

C for Updating an
                                 			 ALI record, such as changing a street name

D for Deleting an
                                 			 ALI record

If you make
                           		changes to an ALI record in Emergency Responder to correct errors reported by
                           		Qwest, you may need to use AFT to change the function code for ELIN records.

For example,
                           		Emergency Responder initially generates ALI records with a function code of I
                           		for Insert. After you format a file and export it to Qwest using AFT, Qwest may
                           		reject the file because of an error. The error may be that the street suffix is
                           		incorrect, for example. You cannot change the street suffix in AFT because this
                           		field is disabled. You must change the ALI record using Emergency Responder.

When
                           		Emergency Responder generates the ALI record the second time after you make the
                           		change, it sets the function code to C because it assumes that the first file
                           		was accepted. Use AFT to change the function code for ELIN records from C to I.
                           		Then, generate the format using AFT and send the reformatted file to Qwest

## ALI Formatting Tool for Verizon

The following sections describe how to use the AFT for Verizon.

### Function Code
                           	 Modifications

Verizon does
                              		not have any service provider-specific fields that you must modify using the
                              		AFT. However, when using AFT to format records for Verizon, you may need to
                              		modify the function code.

Emergency
                              		Responder sets the function code to one of the following:

I—Inserting a new
                                    			 ALI record (the default)

C—Updating an ALI
                                    			 record, such as changing a street name

D—Deleting an ALI
                                    			 record

U—Unlocking an ALI
                                    			 Record (included to support Local Number Portability)

M—Migrating an ALI
                                    			 Record (included to support Local Number Portability)

If you make
                              		changes to an ALI record in Emergency Responder to correct errors reported by
                              		Verizon, you may need to use AFT to change the function code for ELIN records.

For example,
                              		Emergency Responder initially generates ALI records with a function code of I
                              		for Insert. After you format a file and export it to Verizon using AFT, Verizon
                              		may reject the file because of an error. The error may be that the street
                              		suffix is incorrect, for example. You cannot change the street suffix in AFT
                              		because this field is disabled. You must change the ALI record using Emergency
                              		Responder.

When
                              		Emergency Responder generates the ALI record the second time after you make the
                              		change, it sets the function code to C because it assumes that the first file
                              		was accepted. Use AFT to change the function code for ELIN records from C to I.
                              		Then, generate the format using AFT and send the reformatted file to Verizon.

### Verizon New England
                           	 State Disability Indicator Modifications

To make
                                 		  the ELIN records readable by Verizon's New England states (MA, ME, NH, RI, VT),
                                 		  you may need to use AFT to update the Disability Indicator field; this field is
                                 		  specific to Verizon. The Disability Indicator is a reserved 20-character field
                                 		  that the carrier can use to enter disability information.

The
                                 		  following table shows the Disability Indicator designations that you can use to
                                 		  populate the location field of an ALI record.

Disability Indicator

Description

LSS

Life Support System

MI

Mobility Impaired

B

Blind

DHH

Deaf and Hard of Hearing

TTY

Teletypewriter

SI

Speech Impaired

DD

Developmentally Disabled

AFT
                                 		  intelligently identifies the New England states (from the state field of the
                                 		  ALI record) and allows you to update the Disability Indicator field
                                 		  individually (by selecting an New England ELIN record from the tree) or in bulk
                                 		  (through the Bulk Update feature).

### Customer Name for
                           	 Verizon West State Modifications

The Verizon
                              		West states (CA, HI, ID, IL, IN, MI, NC, OH, OR, SC, TX, WA, WI) read the
                              		Customer Name field in the following format which uses a comma followed by a
                              		space between the last name and the first name. For example, Last Name, First
                              		Name.

This format
                              		prevents display errors at the PSAP. You can use AFT to update the field so
                              		that it follows the format that is used by Verizon West states.

AFT
                              		intelligently identifies the Verizon West states (from the state field of the
                              		ALI record) and allows you to update the Customer Name field individually (by
                              		selecting a Verizon West ELIN record from the tree) or in bulk (through the
                              		Bulk Update feature).

When you use
                              		AFT to make updates, it creates two different entries for the Customer Name
                              		field—one in the Emergency Responder database and one in the Service Provider's
                              		database. To avoid future discrepancies, you should also make the same update
                              		in the Customer Name field in the Emergency Responder GUI.

### New Jersey Location
                           	 Modifications

Verizon's
                              		New Jersey (NJ) system is a keyword-driven system that is based on a state
                              		requirement that location data be uniformly displayed at all PSAPs. Data is
                              		extracted from the location field only when one or more keywords, associated
                              		data, and delimiters are present in exact prescribed format. The NJ system
                              		location has four separate and distinct location type fields which can be
                              		simultaneously displayed at the PSAP. The location type fields are as follows:

Unit Type (APT,
                                    			 BOX, LOT, PIER, RM, ROOM, RU, SUIT, SUITE, UNIT, WING)

Floor Number (FLR)

Building
                                    			 Description (BLDG)

Coin Location
                                    			 Description (DES)

AFT
                              		intelligently identifies the NJ system-specific requirement for Location (from
                              		the state field of the ALI record) and allows you to update the location
                              		individually (by selecting a New Jersey ELIN) as well as in bulk (through the
                              		Bulk Update feature).

When you use
                              		AFT to make updates, it creates two different entries for the Customer Name
                              		field—one in the Emergency Responder database and one in the Service Provider's
                              		database. To avoid future discrepancies, you should also make the exact update
                              		in the Location field in Emergency Responder GUI.

| NENA Function Code Field | Bell Canada Transaction Code Field |
|---|---|
| I
                                             					 for Insert a new record. | A
                                             					 for Add a new record. |
| C
                                             					 for Change a record. | A
                                             					 for Change a record. Note The NENA
                                                         						Function Code C is mapped to Bell Canada's Transaction Code A. | Note | The NENA
                                                         						Function Code C is mapped to Bell Canada's Transaction Code A. |
| Note | The NENA
                                                         						Function Code C is mapped to Bell Canada's Transaction Code A. |
| D
                                             					 for Delete a record. | D
                                             					 for Delete a record. |

| Note | The NENA
                                                         						Function Code C is mapped to Bell Canada's Transaction Code A. |
|---|---|

| Note | You do not
                                             			 configure the Language Indicator field using AFT; AFT sets the field to E for
                                             			 English. |
|---|---|

| Field | Description | Format | Notes |
|---|---|---|---|
| Service Class | Type of telephone service of the customer's Terminal Number. | 3
                                             					 alphanumeric characters | Required field. |
| Postal Code | Postal code of the customer's service address. | 6
                                             					 alphanumeric characters | Required field. The first character must be alphabetic. |
| Municipality Code | Unique code assigned to each municipality. | 3
                                             					 alphanumeric characters | Required field. |
| Class of Service | Code that identifies the grade, class, and type of service. | 5
                                             					 alphanumeric characters | Required field. |
| System Source | Identifies the source database of the Transaction Record. | 1
                                             					 alphabetic character | Required field. |
| Location Type | Type of location within a building (for example, apartment). | 15
                                             					 alphanumeric characters | Optional field. |
| Location Number | Number of the location identified in the Location Type field
                                             					 (for example, apartment 2, floor 2). | 6
                                             					 alphanumeric characters | Optional field. |
| Service Municipality | City, town, village, borough, or locality. | 35
                                             					 alphanumeric characters | Required field. |
| LSP
                                             					 ID | Unique code provided to the PS ALI customer by Bell Canada that
                                             					 denotes the provider of local telephone service. | 5
                                             					 alphanumeric characters | Required field. Must be the valid LSP Identifier provided to the PS ALI customer
                                             					 by Bell Canada. |

| Disability Indicator | Description |
|---|---|
| LSS | Life Support System |
| MI | Mobility Impaired |
| B | Blind |
| DHH | Deaf and Hard of Hearing |
| TTY | Teletypewriter |
| SI | Speech Impaired |
| DD | Developmentally Disabled |