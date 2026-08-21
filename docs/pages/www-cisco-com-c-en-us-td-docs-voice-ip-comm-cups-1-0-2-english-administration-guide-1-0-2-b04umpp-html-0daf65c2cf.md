---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b04umpp-html-0daf65c2cf
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b04umpp.html
retrieved_at: 2026-08-21T16:12:36.028052+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: MeetingPlace Profile

## Chapter: MeetingPlace Profile

## MeetingPlace Express Profile

Use Cisco MeetingPlace Express Profile settings to configure settings that are related to Cisco MeetingPlace Express, including primary servers, standby servers, and the users that are associated with the profile. You can use this window to search for specific profiles and change individual settings.

## Finding a Cisco MeetingPlace Express Profile

Because you might have several Cisco MeetingPlace Express profiles in your network, Cisco Unified Presence Server lets you locate specific Cisco MeetingPlace Express profiles on the basis of specific criteria. Use the following procedure to locate specific Cisco MeetingPlace Express profiles.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Application > Unified Personal Communicator > MeetingPlace Express Profile .

The Find and List MeetingPlace Express Profiles window displays. Use the drop-down list box to search for Cisco MeetingPlace Express profiles.

Step 2 From the drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 3 Specify the appropriate search text, if applicable, and click Find .

Tip To find all Cisco MeetingPlace Express profiles that are registered in the database, click Find without entering any search text.

A list of discovered Cisco MeetingPlace Express profiles displays.

Step 4 From the list of records, click the Cisco MeetingPlace Express profile that matches your search criteria.

The window displays the Cisco MeetingPlace Express profile that you choose.

Additional Information

See the "Related Topics" section .

## Configuring a Cisco MeetingPlace Express Profile

This section describes how to add or update a Cisco MeetingPlace Express profile in the Cisco Unified Presence Server database.

Step 1 Perform one of the following tasks:

• To add a Cisco MeetingPlace Express profile, choose Application > Unified Personal Communicator > MeetingPlace Express Profile and click Add New .

• To update a Cisco MeetingPlace Express profile, find the profile by using the procedure in the "Finding a Cisco MeetingPlace Express Profile" section .

The MeetingPlace Express Profile Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 28-1 .

Step 3 To associate users with the Cisco MeetingPlace Express profile, click Add Users to Profile .

The Find and List Users window displays.

Step 4 From the first drop-down list box, choose one of the following criteria:

• First name

• Middle name

• Last name

• User ID

• Department

Step 5 From the second drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 6 Specify the appropriate search text, if applicable, and click Find .

Tip To find all users that are registered in the database, click Find without entering any search text.

A list of discovered users displays.

Step 7 From the list of records, click the users that you want to add to the Cisco MeetingPlace Express profile or click Select All .

Step 8 To add the users to the Cisco MeetingPlace Express profile, click Add Selected .

Step 9 To exit the Find and List Users window, click Close .

Step 10 To save the data and to add the Cisco MeetingPlace Express profile to the database, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## Cisco MeetingPlace Express Profile Configuration Settings

Table 28-1 describes the Cisco MeetingPlace Express profile configuration parameters. For related procedures, see the "Related Topics" section .

Table 28-1 Cisco MeetingPlace Express Profile Configuration Parameters

Name

This parameter specifies the name of the Cisco MeetingPlace Express profile.

Maximum characters: 128

Description

This parameter provides a general description of the Cisco MeetingPlace Express profile.

Maximum characters: 128

Primary MeetingPlace Express Server

This parameter specifies the primary Cisco MeetingPlace Express server. From the dropdown list, you can choose from the Cisco MeetingPlace Express servers that you have already defined on the system.

Backup MeetingPlace Express Server

This parameter specifies the backup Cisco MeetingPlace Express server. From the dropdown list, you can choose from the Cisco MeetingPlace Express servers that you have already defined on the system. You can specify two backup Cisco MeetingPlace Express servers.

## Deleting a Cisco MeetingPlace Express Profile

This section describes how to delete a Cisco MeetingPlace Express profile.

Step 1 Find the Cisco MeetingPlace Express profile by using the procedure in the "Finding a Cisco MeetingPlace Express Profile" section .

Step 2 From list of matching records, choose the Cisco MeetingPlace Express profile that you want to delete.

Step 3 To delete the profile, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the Cisco MeetingPlace Express profile is not in use, Cisco Unified Presence Server deletes it. If it is in use, a message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding a Cisco MeetingPlace Express Profile

• Configuring a Cisco MeetingPlace Express Profile

• Deleting a Cisco MeetingPlace Express Profile

| Field | Description |
|---|---|
| Name | This parameter specifies the name of the Cisco MeetingPlace Express profile. Maximum characters: 128 |
| Description | This parameter provides a general description of the Cisco MeetingPlace Express profile. Maximum characters: 128 |
| Primary MeetingPlace Express Server | This parameter specifies the primary Cisco MeetingPlace Express server. From the dropdown list, you can choose from the Cisco MeetingPlace Express servers that you have already defined on the system. |
| Backup MeetingPlace Express Server | This parameter specifies the backup Cisco MeetingPlace Express server. From the dropdown list, you can choose from the Cisco MeetingPlace Express servers that you have already defined on the system. You can specify two backup Cisco MeetingPlace Express servers. |