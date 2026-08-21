---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b04uctip-html-cccad9ba6d
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b04uctip.html
retrieved_at: 2026-08-21T16:12:43.889154+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: CTI Gateway Profile

## Chapter: CTI Gateway Profile

## CTI Gateway Profile

Use CTI gateway profile settings to configure settings that are related to the CTI gateway, including primary servers, standby servers, and the users that are associated with the profile. You can use this window to search for specific profiles and change individual settings.

## Finding a CTI Gateway Profile

Because you might have several CTI gateway profiles in your network, Cisco Unified Presence Server lets you locate specific CTI gateway profiles on the basis of specific criteria. Use the following procedure to locate specific CTI gateway profiles.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Application > Unified Personal Communicator > CTI Gateway Profile .

The Find and List CTI Gateway Profiles window displays. Use the two drop-down list boxes to search for CTI gateway hosts.

Step 2 From the first drop-down list box, choose one of the following criteria:

• Name

• Description

Step 3 From the drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 4 Specify the appropriate search text, if applicable, and click Find .

Tip To find all CTI gateway profiles that are registered in the database, click Find without entering any search text.

A list of discovered CTI gateway profiles displays.

Step 5 From the list of records, click the CTI gateway profile that matches your search criteria.

The window displays the CTI gateway profile that you choose.

Additional Information

See the "Related Topics" section .

## Configuring a CTI Gateway Profile

This section describes how to add or update a CTI gateway profile in the Cisco Unified Presence Server database.

Step 1 Perform one of the following tasks:

• To add a CTI gateway profile, choose Application > Unified Personal Communicator > CTI Gateway Profile and click Add New .

• To update a CTI gateway profile, find the profile by using the procedure in the "Finding a CTI Gateway Profile" section .

The CTI Gateway Profile Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 30-1 .

Step 3 To associate users with the CTI gateway profile, click Add Users to Profile .

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

Tip To find all user profiles that are registered in the database, click Find without entering any search text.

A list of discovered user profiles displays.

Step 7 From the list of records, click the users that you want to add to the CTI gateway profile or click Select All .

Step 8 To add the users to the CTI gateway profile, click Add Selected .

Step 9 To exit the Find and List Users window, click Close .

Step 10 To save the data and to add the CTI gateway profile to the database, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## CTI Gateway Profile Configuration Settings

Table 30-1 describes the CTI gateway profile configuration parameters. For related procedures, see the "Related Topics" section .

Table 30-1 CTI Gateway Profile Configuration Parameters

Name

This parameter specifies the name of the CTI gateway profile.

Description

This parameter provides a general description of the CTI gateway profile.

Primary CTI Gateway Server

This parameter specifies the primary CTI gateway server. From the dropdown list, you can choose from the CTI gateway servers that you have already defined on the system.

Backup CTI Gateway Server

This parameter specifies the backup CTI gateway server. From the dropdown list, you can choose from the of CTI gateway servers that you have already defined on the system. You can specify two backup CTI gateway servers.

## Deleting a CTI Gateway Profile

This section describes how to delete a CTI gateway profile.

Step 1 Find the CTI gateway profile by using the procedure in the "Finding a CTI Gateway Profile" section .

Step 2 From list of matching records, choose the CTI gateway profile that you want to delete.

Step 3 To delete the CTI gateway profile, Click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the CTI gateway profile is not in use, Cisco Unified Presence Server deletes it. If it is in use, a message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding a CTI Gateway Profile

• Configuring a CTI Gateway Profile

• Deleting a CTI Gateway Profile

| Field | Description |
|---|---|
| Name | This parameter specifies the name of the CTI gateway profile. |
| Description | This parameter provides a general description of the CTI gateway profile. |
| Primary CTI Gateway Server | This parameter specifies the primary CTI gateway server. From the dropdown list, you can choose from the CTI gateway servers that you have already defined on the system. |
| Backup CTI Gateway Server | This parameter specifies the backup CTI gateway server. From the dropdown list, you can choose from the of CTI gateway servers that you have already defined on the system. You can specify two backup CTI gateway servers. |