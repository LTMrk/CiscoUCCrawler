---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-aft-1-1-english-sbc-ameritech-user-guide-user-ame-afterror-html-8a8aa35b2f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/aft/1_1/english/sbc_ameritech/user/guide/user_ame/AFTerror.html
retrieved_at: 2026-08-21T15:51:02.971577+00:00
---

ALI Formatting Tool User Guide for SBC Ameritech

# ALI Formatting Tool User Guide for SBC Ameritech

Updated: November 2, 2007

Chapter: Troubleshooting the ALI Formatting Tool

## Chapter: Troubleshooting the ALI Formatting Tool

## Troubleshooting the ALI Formatting Tool

These topics address problems you might encounter using the ALI Formatting Tool (AFT) and provide ways to resolve them:

• Collecting Error and Trace Messages

• Troubleshooting AFT Problems

• Frequently Asked Questions

## Collecting Error and Trace Messages

The ALI Formatting Tool (AFT) logs errors, warnings, record changes, and information messages using a logging device that is similar to the one that Cisco Emergency Responder (Cisco ER) uses.

Note Un-installing AFT does not remove the AFT logs. This allows you to use the logs to find details about old AFT transactions.

For bulk operations, AFT logs information related to the bulk operation, not individual record updates.

You can access the AFT logs, in one of two ways. Go to:

• the log folder at:

C:\ProgramFiles\CiscoSystems\AFT\logs\< providername >

• the install folder at:

C:\Program Files\CiscoSystems\AFT\< providername >

and follow the shortcut to the AFT logs.

Related Topics

• Troubleshooting AFT Problems

• Frequently Asked Questions

## Troubleshooting AFT Problems

Use the following sections to resolve AFT problems:

• Cannot Install AFT

• Cannot Log In To AFT

• Cannot Locate the AFT Logs

### Cannot Install AFT

Problem: You receive an error message when you try to install AFT on a Windows 2000 system.

Action: Cisco Emergency Responder (Cisco ER) must be installed before you can install AFT. You must install AFT on the same server with Cisco ER.

Make sure that Cisco ER is installed, then try to install AFT again.

### Cannot Log In To AFT

Problem: You get an "Invalid Login" message when you try to log in to AFT.

Action: You must be a member of CERSystemAdmin and CERERLAdminGroup for Cisco Emergency Responder (Cisco ER). Check the group membership at:

Start > Control Panel > Administrative Tools > Computer Management > Users and Groups > Groups

### Cannot Locate the AFT Logs

Problem: You cannot find the AFT Logs.

Action: The ALI Formatting Tool (AFT) is installed in:

C:\Program Files\CiscoSystems\AFT\< providername >

Follow the shortcut in this folder to the AFT Log Folder.

All AFT logs are saved here:

C:\ProgramFiles\CiscoSystems\AFT\logs\< providername >

Related Topics

• Collecting Error and Trace Messages

• Frequently Asked Questions

## Frequently Asked Questions

Q. My Service Provider accepts NENA 2.0 files. From the Cisco Emergency Responder (Cisco ER) documentation, I see that Cisco ER itself generates NENA 2.0 files. Will I need to use AFT for sending ALI files to my service provider?

A. Cisco ER was designed to generate ALI files in NENA 2.0, 2.1 and 3.0 format. However, many service providers have specific fields that they use for internal purposes. If their fields are missing, they might reject the ALI file you send them from Cisco ER. These ALI files need formatting for the service provider-specific fields. This might be adding, removing, or changing the position of some fields. AFT is a small application that you can download from CCO and use for formatting the ALI files which Cisco ER generates according to your service provider's requirements.

Q. In my Cisco ER setup, I have a set of ELINs that I bought from SBC Ameritech (Ameritech) and another set of ELINs that I bought from Sprint. I have configured these ELINs in Cisco ER. I did an ALI export and exported the ELINs to a single file. How will I send this ELIN file separately to Ameritech and Sprint?

A. You can use AFT to accomplish this task. Perform the following steps:

Step 1 Download the AFT for Ameritech and download the AFT for Sprint from CCO and install them on your Cisco ER server.

Step 2 Give the ALI file exported from Cisco ER as input to the Ameritech AFT.

Step 3 Perform the necessary formatting selectively for the Ameritech ELINs:

Step 4 Use the Ameritech Area Code which is different from the Sprint area code. Send this file of the Ameritech ELINs to Ameritech.

Step 5 Repeat steps 2 - 4 to generate a file containing just the Sprint ELINs by using AFT for Sprint.

Related Topics

• Collecting Error and Trace Messages

• Troubleshooting AFT Problems