---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-aft-1-1-english-sbc-pacbell-user-guide-user-sbc-pb-html-692061c292
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/aft/1_1/english/sbc_pacbell/user/guide/user_sbc/PB.html
retrieved_at: 2026-08-21T15:51:36.714013+00:00
---

ALI Formatting Tool User Guide for SBC Pacific Bell

# ALI Formatting Tool User Guide for SBC Pacific Bell

Updated: November 2, 2007

Chapter: Using the ALI Formatting Tool for SBC Pacific Bell

## Chapter: Using the ALI Formatting Tool for SBC Pacific Bell

- Enabling Call Back For This ELIN

- Changing the Function Code

## Using the ALI Formatting Tool for SBC Pacific Bell

This section provides information about how to set up the AFT fields that are specific to SBC Pacific Bell (PacBell). Use this information along with "Using the ALI Formatting Tool" to generate ALI files in a format that SBC Pacific Bell can use to update their ELIN records.

These topics provide information for the PacBell-specific format:

• Enabling Call Back For This ELIN

• Changing the Function Code

## Enabling Call Back For This ELIN

Cisco Emergency  Responder (Cisco ER) displays the emergency location identification number ( ELIN) at the public safety answering point (PSAP). The PSAP can then dial to reconnect to the emergency caller if the emergency call is cut off for any reason, or if the PSAP simply needs to talk to the caller again.

The Call Back for this ELIN option allows you to specify a direct inward dial (DID) number that can be called back by the PSAP when a call from a fictitious number is made to 911.

The Call Back for this ELIN option performs two important functions:

• It alerts the PSAP that the phone they are calling back may not have generated the 911 call.

• It enables the PSAP to call back to a phone that is located near the fictitious telephone number that did place the call.

Cisco recommends that you always enable this option by checking the Call Back for this ELIN field. (The default is to leave the field blank which defaults to no.)

## Changing the Function Code

Cisco Emergency  Responder (Cisco ER) sets the Function Code to one of the following:

• I for Inserting a new ALI record (the default)

• C for Updating an ALI record, such as changing a street name

• D for Deleting an ALI record

If you make changes to an ALI record in Cisco ER to correct errors reported by your service provider, you may need to use AFT to change the Function Code for ELIN records. The following provides an example of when you need to change the function code.

Example A-1 Changing the Function Code

Cisco Emergency  Responder initially generates ALI records with a function code of I, for insert. After you format a file and export it to SBC Pacific Bell (PacBell) using AFT, PacBell may reject the file. The error may be that the street suffix is incorrect, for example. You cannot change the street suffix in AFT because this field is disabled in AFT. You must change the ALI record using Cisco ER.

When Cisco ER generates the ALI record the second time after you make the change, it sets the Function Code to C because it assumes that the first file was accepted. Use AFT to change the Function Code for ELIN records from C to I.

Then, generate the format using AFT, and send the reformatted file to PacBell.