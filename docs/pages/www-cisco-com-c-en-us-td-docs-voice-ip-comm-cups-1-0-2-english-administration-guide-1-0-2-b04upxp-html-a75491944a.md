---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b04upxp-html-a75491944a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b04upxp.html
retrieved_at: 2026-08-21T16:12:56.736956+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Proxy Profile

## Chapter: Proxy Profile

## Proxy Profile

Use proxy profile settings to configure settings that are related to the SIP proxy server, including primary servers, standby servers, and the users that are associated with the profile. You can use this window to search for specific profiles and change individual settings.

## Finding a Proxy Profile

Because you might have several proxy profiles in your network, Cisco Unified Presence Server lets you locate specific proxy profiles on the basis of specific criteria. Use the following procedure to locate specific proxy profiles.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Application > Unified Personal Communicator > Proxy Profile .

The Find and List Proxy Profiles window displays. Use the drop-down list boxes to search for proxy profiles.

Step 2 From the first drop-down box, choose one of the following criteria:

• Name

• Description

Step 3 From the second drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 4 Specify the appropriate search text, if applicable, and click Find .

Tip To find all proxy profiles that are registered in the database, click Find without entering any search text.

A list of discovered proxy profiles displays.

Step 5 From the list of records, click the proxy profile that matches your search criteria.

The window displays the proxy profile that you choose.

Additional Information

See the "Related Topics" section .

## Configuring a Proxy Profile

This section describes how to add or update a proxy profile in the Cisco Unified Presence Server database.

Step 1 Perform one of the following tasks:

• To add a proxy profile, choose Application > Unified Personal Communicator > Proxy Profile and click Add New .

• To update a proxy profile, find the profile by using the procedure in the "Finding a Proxy Profile" section .

The Proxy Profile Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 33-1 .

Step 3 To associate users with the proxy profile, click Add Users to Profile .

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

Step 7 From the list of records, click the users that you want to add to the proxy profile or click Select All .

Step 8 To add the users to the proxy profile, click Add Selected .

Step 9 To exit the Find and List Users window, click Close .

Step 10 To save the data and to add the proxy profile to the database, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## Proxy Profile Configuration Settings

Table 33-1 describes the proxy profile configuration parameters. For related procedures, see the "Related Topics" section .

Table 33-1 proxy Profile Configuration Parameters

Name

This parameter specifies the name of the proxy profile.

Description

This parameter provides a general description of the proxy profile.

Primary Proxy Server

This parameter specifies the primary proxy server. From the dropdown list, you can choose from the proxy servers that you already defined on the system.

Backup Proxy Server

This parameter specifies the backup proxy server. From the dropdown list, you can choose from the proxy servers that you already defined on the system. You can specify two backup proxy servers.

## Deleting a Proxy Profile

This section describes how to delete a proxy profile.

Step 1 Find the proxy profile by using the procedure in the "Finding a Proxy Profile" section .

Step 2 From list of matching records, choose the proxy profile that you want to delete.

Step 3 To delete the profile, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the proxy profile is not in use, Cisco Unified Presence Server deletes it. If it is in use, a message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding a Proxy Profile

• Configuring a Proxy Profile

• Deleting a Proxy Profile

| Field | Description |
|---|---|
| Name | This parameter specifies the name of the proxy profile. |
| Description | This parameter provides a general description of the proxy profile. |
| Primary Proxy Server | This parameter specifies the primary proxy server. From the dropdown list, you can choose from the proxy servers that you already defined on the system. |
| Backup Proxy Server | This parameter specifies the backup proxy server. From the dropdown list, you can choose from the proxy servers that you already defined on the system. You can specify two backup proxy servers. |