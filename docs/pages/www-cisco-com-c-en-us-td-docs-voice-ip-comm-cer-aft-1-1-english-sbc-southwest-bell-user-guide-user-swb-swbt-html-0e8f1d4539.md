---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-aft-1-1-english-sbc-southwest-bell-user-guide-user-swb-swbt-html-0e8f1d4539
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/aft/1_1/english/sbc_southwest_bell/user/guide/user_swb/SWBT.html
retrieved_at: 2026-08-21T15:50:08.622559+00:00
---

ALI Formatting Tool User Guide for SBC Southwestern Bell

# ALI Formatting Tool User Guide for SBC Southwestern Bell

Updated: November 2, 2007

Chapter: Using the ALI Formatting Tool for SBC Southwestern Bell

## Chapter: Using the ALI Formatting Tool for SBC Southwestern Bell

- Modifying PS Code for SBC Southwestern Bell

- Changing the Function Code

## Using the ALI Formatting Tool for SBC Southwestern Bell

This section provides information about how to set up the AFT fields that are specific to SBC Southwestern Bell. Use this information along with "Using the ALI Formatting Tool" to generate ALI files in a format that SBC Southwestern Bell can use to update their ELIN records.

• Modifying PS Code for SBC Southwestern Bell

• Changing the Function Code

## Modifying PS Code for SBC Southwestern Bell

In order to make the ELIN records readable by SBC Southwestern Bell, you may need to use AFT to update the SBC Southwestern Bell-specific field, PS Code.

The PS Code is a four-digit code that the SBC Southwestern Bell system assigns whenever the system configures a new PS site. This code is associated with the PS user's login and source. The PS Code is a feature that allows only records with the correct PS Code to be processed into tables for the PS Site.

If the PS Code does not match the configurations for the Source Name that is assigned to the PS Site, the record will not process. Before you generate a formatted file using AFT, make sure that PS Code and the Source Name match.

For more information, refer to the SBC Southwestern Bell documentation.

## Changing the Function Code

Cisco Emergency Responder (Cisco ER) sets the Function Code to one of the following:

• I for Inserting a new ALI record (the default)

• C for Updating an ALI record, such as changing a street name

• D for Deleting an ALI record

If you make changes to an ALI record in Cisco ER to correct errors reported by your service provider, you may need to use AFT to change the Function Code for ELIN records. Example A-1 illustrates when you need to change the function code.

Example A-1 Changing the Function Code

Cisco ER initially generates ALI records with a function code of I, for insert. After you format a file and export it to SBC Southwestern Bell using AFT, SBC Southwestern Bell may reject the file. The error may be that the street suffix is incorrect, for example. You cannot change the street suffix in AFT because this field is disabled in AFT. You must change the ALI record using Cisco ER.

When Cisco ER generates the ALI record the second time after you make the change, it sets the Function Code to C because it assumes that the first file was accepted. Use AFT to change the Function Code for ELIN records from C to I.

Then, generate the format using AFT, and send the reformatted file to SBC Southwestern Bell.