---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cer-aft-1-1-english-bell-canada-user-guide-user-can-afterrors-html-ef8e4cf29b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cer/aft/1_1/english/bell_canada/user/guide/user_can/AFTerrors.html
retrieved_at: 2026-08-21T15:50:33.794485+00:00
---

ALI Formatting Tool User Guide for Bell Canada

# ALI Formatting Tool User Guide for Bell Canada

Updated: November 2, 2007

Chapter: Troubleshooting the ALI Formatting Tool

## Chapter: Troubleshooting the ALI Formatting Tool

## Troubleshooting the ALI Formatting Tool

These topics address problems you might encounter using the ALI Formatting Tool (AFT) and provide ways to resolve them:

• Collecting Error and Trace Messages

• Troubleshooting AFT Problems

## Collecting Error and Trace Messages

The ALI Formatting Tool (AFT) logs errors, warnings, record changes, and information messages using a logging device that is similar to the one that Emergency Responder uses.

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

## Troubleshooting AFT Problems

Use the following sections to resolve AFT problems:

• Cannot Install AFT

• Cannot Log In To AFT

• Cannot Locate the AFT Logs

### Cannot Install AFT

Problem: You receive an error message when you try to install AFT on a Windows 2000 system.

Action: Cisco Emergency Responder (Cisco ER) must be installed before you can install AFT. You must install AFT on the same server with Cisco ER.

Make sure that Cisco ERis installed, then try to install AFT again.

### Cannot Log In To AFT

Problem: You get an "Invalid Login" message when you try to log in to AFT.

Action: You must be a member of CERSystemAdmin and CERERLAdminGroup for Cisco Emergency Cisco Responder. Check the group membership at:

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