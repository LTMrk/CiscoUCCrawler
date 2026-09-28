---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-aft-1-1-english-verizon-user-guide-user-ver-verizon-html-05c8f160a2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/aft/1_1/english/verizon/user/guide/user_ver/verizon.html
retrieved_at: 2026-08-21T15:52:06.696707+00:00
---

ALI Formatting Tool User Guide for Verizon

# ALI Formatting Tool User Guide for Verizon

Chapter: Using the ALI Formatting Tool for Verizon

## Chapter: Using the ALI Formatting Tool for Verizon

## Using the ALI Formatting Tool for Verizon

This section provides information about how to set up the AFT fields that are specific to Verizon. Use the following information along with "Using the ALI Formatting Tool" to generate ALI files in a format that Verizon can use to update their ELIN records.

## Changing the Function Code

Cisco Emergency Responder (Cisco ER) sets the Function Code to one of the following:

• I—Inserting a new ALI record (the default)

• C—Updating an ALI record, such as changing a street name

• D—Deleting an ALI record

• U—Unlocking an ALI Record (included to support Local Number Portability)

• M—Migrating an ALI Record (included to support Local Number Portability)

If you make changes to an ALI record in Cisco ER to correct errors reported by Verizon, you may need to use AFT to change the Function Code for ELIN records.

Example A-1 illustrates when you need to change the Function Code.

Example A-1 Changing the Function Code

Cisco ER initially generates ALI records with a Function Code of I, for insert. After you format a file and export it to Verizon using AFT, Verizon may reject the file because of an error. The error may be that the street suffix is incorrect, for example. You cannot change the street suffix in AFT because this field is disabled in AFT. You must change the ALI record using Cisco ER.

When Cisco ER generates the ALI record the second time after you make the change, it sets the Function Code to C because it assumes that the first file was accepted. Use AFT to change the Function Code for ELIN records from C to I. Then, generate the format using AFT, and send the reformatted file to Verizon.

## Modifying the Disability Indicator for Verizon New England States

To make the ELIN records readable by Verizon's New England states (MA, ME, NH, RI, VT), you may need to use AFT to update the Verizon specific field—Disability Indicator. The Disability Indicator is a reserved 20 character field that the carrier can use to enter disability information. Table A-1 shows the Disability Indicator designations that you can use to populate the location field of an ALI record:

Table A-1 Disability Indicator

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

AFT intelligently identifies the New England states (from the state field of the ALI record) and it allows you to update the Disability Indicator field both individually (by selecting an New England ELIN record from the tree) or in bulk (through the Bulk Update feature). For more information on using the Bulk Update feature, see the task " Perform a bulk update to the ALI files" in the "Using the Tool Bar and Icons" section .

## Modifying the Customer Name for Verizon West States

The Verizon West states (CA, HI, ID, IL, IN, MI, NC,OH, OR, SC, TX, WA,WI) read the Customer Name field in the following format that uses a comma followed by a space between the last name and the first name:

Last Name, First Name

This format prevents display errors at the PSAP. You can use AFT to update the field so that it follows the format that is used by Verizon West states.

AFT intelligently identifies the Verizon West states (from the state field of the ALI record) and allows you to update the Customer Name field both individually (by selecting a Verizon West ELIN record from the tree) or in bulk (through the Bulk Update feature). For more information on using the Bulk Update feature, see the task " Perform a bulk update to the ALI files" in the "Using the Tool Bar and Icons" section .

When you use AFT to make updates, it creates two different entries for the Customer Name field—one in the CER database and one in the Service Provider's database. To avoid future discrepancies, you should also make the same update in the Customer Name field in the CER GUI too. To assure this, AFT displays a warning in its GUI to copy the updated value and paste it in Customer Name field of the selected ELIN in the CER's ALI details form.

## Modifying the Location for New Jersey

Verizon's New Jersey (NJ) system is a keyword driven system that is based on a state requirement that location data be uniformly displayed at all PSAPs. Data is extracted from the location field, only when one or more keywords, associated data, and delimiters are present in exact prescribed format. The NJ system location has four separate and distinct location type fields which can be simultaneously displayed at the PSAP. They are as follows:

• Unit Type (APT, BOX, LOT, PIER, RM, ROOM, RU, SUIT, SUITE, UNIT, WING)

• Floor Number (FLR)

• Building Description (BLDG)

• Coin Location Description (DES)

AFT intelligently identifies the NJ system specific requirement for Location (from the state field of the ALI record) and allows you to update the location individually (by selecting a New Jersey ELIN from tree) as well as in bulk (through the Bulk Update feature). For more information on using the Bulk Update feature, see the task " Perform a bulk update to the ALI files" in the "Using the Tool Bar and Icons" section .

When you use AFT to make updates, it creates two different entries for the Customer Name field—one in the CER database and one in the Service Provider's database. To avoid future discrepancies, you should also make the exact update in the Location field in CER GUI. To assure this, AFT displays a warning in its GUI to copy the updated value and paste it in Location field of the selected ELIN in the CER's ALI details form.

| Disability Indicator | Description |
|---|---|
| LSS | Life Support System |
| MI | Mobility Impaired |
| B | Blind |
| DHH | Deaf and Hard of Hearing |
| TTY | Teletypewriter |
| SI | Speech Impaired |
| DD | Developmentally Disabled |