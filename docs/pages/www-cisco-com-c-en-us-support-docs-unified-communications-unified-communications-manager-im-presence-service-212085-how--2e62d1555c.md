---
doc_id: www-cisco-com-c-en-us-support-docs-unified-communications-unified-communications-manager-im-presence-service-212085-how--2e62d1555c
source_url: https://www.cisco.com/c/en/us/support/docs/unified-communications/unified-communications-manager-im-presence-service/212085-How-to-Utilize-BAT-to-Update-Cisco-Jabbe.html
retrieved_at: 2026-08-16T23:37:15.260912+00:00
---

Utilize BAT to Update Jabber Contact List

# Utilize BAT to Update Jabber Contact List

### Download Options

Updated: September 14, 2017

Document ID: 212085

Contents

## Contents

## Introduction

This document describes how to use BAT (Bulk Administration Tool) to  add or update a new contact list for a Jabber enduser.

## Prerequisites

### Requirements

Cisco recommends that you have knowledge of these topics:

- LDAP ( Lightweight Directory Access Protocol )

- Cisco Instant Messaging and Presence Server (IM&P)

### Components Used

The information in this document is based on these software versions:

- Cisco Instant Messaging and Presence Server

The information in this document was created from the devices in a specific lab environment. All of the devices used in this document started with a cleared (default) configuration. If your network is live, ensure that you understand the potential impact of any command.

## Configuration

Add or update the contact list with new contacts for a jabber user assigned to a IM&P Subscriber. Example from lab environment is shown where LDAPUSER2 's contact list is updated with 3 new contacts i.e LDAPUSER8 , LDAPUSER9 and LDAPUSER10.

Step 1. Navigate to Bulk Administration > Contact List > Export Contact List

Step 2.  Select option Assigned users by node and then select IM&P Subscriber and then select Find . This lists all the users assigned to IM&P Subscriber.

Step 3. Select Next and it save the CSV file on your desktop. This exports all the contact lists for all the users from IM&P SUB. See this image:

Note : You can navigate to Job Scheduler page on IM&P server to check if files was exported without errors or not.

Step 4. Naviagte to Bulk Adminstrator > Upload/Download section and download the exported files which was created in Step 3.

Step 5. As per this article, you add the new contacts list for 1 user, that is LDAPUSER2, however, this is not restricted to single enduser. You can update/add for multiple or all endusers at same time. From the lab, the exported CSV file looks like this:

Note : This shows that LDAPUSER2 has only 1 contact in its list with contact ID as "LDAPUSER1" under group name "contacts". You modified this same file and added 3 more contacts for LDAPUSER2. These 3 contacts are LDAPUSER8 , LDAPUSER9 and LDAPUSER10. Refer this image from newly made CSV file:

Note : You can use the sample CSV file to update/add the contact list for any contact. This file does not require to export any file from IM&P server.

Step 6. After you have updated the CSV file for LDAPUSER2 with new contacts then upload it on IM&P server. Navigate to Bulk Administration > Upload/Download Files.

Note : Use the same option as in the image for Select The Target User Contact List and Select Transaction Type as Import User's Contacts -Custom File and then save/upload it.

Step 7. Navigate to Bulk Administration > Contact List > Update Contact List based on this image.

Step 9. Select Run Immediately or Run Later based on your convenience and then select on Submit. Refer to Job scheduler to check the status of Import.

So LDAPUSER1 was with only one contact but after the import of new CSV file, LDAPUSER2's contact list was updated without even sign out of jabber.

## Things to Remember

- Before the import of new CSV file, the three added users, that is LDAPUSER 8 , LDAPUSER9 and LDAPUSER10, must be enabled for presence capabilities else they do not show up in the contact list of any jabber enduser.

- If you noticed that CSV file doest not have any Colum with a name Telephone Number , still LDAPUSER2's jabber account can fetch the details like Telephone number once it is been imported with new CSV file. This is because when you add the new contacts via BAT, Jabber tries to resolve them through Directory source. So if the newly added contacts are present in Directory Source then Jabber fetches their telephone numbers. For example, LDAPUSER2 Jabber was able to fetch the Telephone Number of LDAPUSER8 via Directory Source as shown in this image:

## Related Information

- Technical Support & Documentation - Cisco Systems

### Revision History

1.0

14-Sep-2017

Initial Release

### Contributed by Cisco Engineers

Varundeep Chhatwa

Cisco TAC Engineer

Edited by Jimit Dalal and Jasmeet Sandhu

Cisco TAC Engineer

### This Document Applies to These Products

- Unified Communications Manager IM & Presence Service

| Revision | Publish Date | Comments |
|---|---|---|
| 1.0 | 14-Sep-2017 | Initial Release |