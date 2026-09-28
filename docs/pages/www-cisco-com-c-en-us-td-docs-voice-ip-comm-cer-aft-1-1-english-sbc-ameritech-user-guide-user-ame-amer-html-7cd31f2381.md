---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-aft-1-1-english-sbc-ameritech-user-guide-user-ame-amer-html-7cd31f2381
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/aft/1_1/english/sbc_ameritech/user/guide/user_ame/amer.html
retrieved_at: 2026-08-21T15:51:07.114921+00:00
---

ALI Formatting Tool User Guide for SBC Ameritech

# ALI Formatting Tool User Guide for SBC Ameritech

Updated: November 2, 2007

Chapter: Using the ALI Formatting Tool for SBC Ameritech

## Chapter: Using the ALI Formatting Tool for SBC Ameritech

## Using the ALI Formatting Tool for SBC Ameritech

SBC Ameritech (Ameritech) does not have any service provider-specific fields that you must modify using the ALI Formatting Tool (AFT). However, when using AFT to format records for Ameritech, you may need to modify the Function Code. Use the following information along with Chapter 3 "Using the ALI Formatting Tool" to generate ALI files in a format that Ameritech can use to update their ELIN records.

Changing the Function Code

Cisco Emergency Responder (Cisco ER) sets the Function Code to one of the following:

• I for Inserting a new ALI record (the default)

• C for Updating an ALI record, such as changing a street name

• D for Deleting an ALI record

If you make changes to an ALI record in Cisco ER to correct errors reported by Ameritech, you may need to use AFT to change the Function Code for ELIN records.

Cisco ER initially generates ALI records with a function code of I, for insert. After you format a file and export it to Ameritech using AFT, Ameritech may reject the file because of an error. The error may be that the street suffix is incorrect, for example. You cannot change the street suffix in AFT because this field is disabled in AFT. You must change the ALI record using Cisco ER.

When Cisco ER generates the ALI record the second time after you make the change, it sets the Function Code to C because it assumes that the first file was accepted. Use AFT to change the Function Code for ELIN records from C to I.

Then, generate the format using AFT, and send the reformatted file to Ameritech.