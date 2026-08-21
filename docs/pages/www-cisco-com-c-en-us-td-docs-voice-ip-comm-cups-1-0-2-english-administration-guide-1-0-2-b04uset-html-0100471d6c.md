---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b04uset-html-0100471d6c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b04uset.html
retrieved_at: 2026-08-21T16:12:18.816312+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: User Settings

## Chapter: User Settings

## User Settings

Use user settings to configure various per-user settings for Cisco Unified Personal Communicator. You can use this window to search for specific users and change individual settings.

## Finding a User

Because you might have several users in your network, Cisco Unified Presence Server lets you locate specific users on the basis of specific criteria. Use the following procedure to locate specific users.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Application > Unified Personal Communicator > User Settings .

The Unified Personal Communicator User Settings Find and List window displays. Use the two drop-down list boxes to search for users.

Step 2 From the first drop-down list box, choose one of the following criteria:

• First Name

• Last Name

• Manager

• Department

From the second drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 3 Specify the appropriate search text, if applicable, and click Find .

Tip To find all users that are registered in the database, click Find without entering any search text.

A list of discovered users displays.

Step 4 From the list of records, click the user that matches your search criteria.

The window displays the user that you choose.

Additional Information

See the "Related Topics" section .

## Configuring a User

This section describes how to add or update users in the Cisco Unified Presence Server database.

Step 1 Perform the following task:

• To update a user, find the user by using the procedure in the "Finding a User" section .

The Unified Personal Communicator User Settings window displays.

Step 2 Enter the appropriate settings as described in Table 24-1 .

Step 3 To save the data and to add the user to the database, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## User Configuration Settings

Table 24-1 describes the user settings configuration parameters. For related procedures, see the "Related Topics" section .

Table 24-1 User Settings Configuration Parameters

Preferred CTI Device

This parameter comprises a dropdown list of the available devices controlled by the user.

Unity Connection Profile

This parameter comprises a dropdown list of the available Cisco Unity Connection profiles. If the list is empty, you may need to configure a Cisco Unity Connection profile for Cisco Unified Personal Communicator.

MeetingPlace Express Profile

This parameter comprises a dropdown list of the available Cisco MeetingPlace Express profiles. If the list is empty, you may need to configure a Cisco MeetingPlace Express profile for Cisco Unified Personal Communicator.

CTI Gateway Profile

This parameter comprises a dropdown list of the available Cisco CTI gateway profiles. If the list is empty, you may need to configure a Cisco CTI gateway profile for Cisco Unified Personal Communicator.

LDAP Profile

This parameter comprises a dropdown list of the available Cisco LDAP profiles. If the list is empty, you may need to configure a Cisco LDAP profile for Cisco Unified Personal Communicator.

SIP Proxy Profile

This parameter comprises a dropdown list of SIP proxy profiles and can be empty.

## Deleting a User

This section describes how to delete a user.

Step 1 Find the user by using the procedure in the "Finding a User" section .

Step 2 From list of matching records, choose the user that you want to delete.

Step 3 To delete the user, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the user is not in use, Cisco Unified Presence Server deletes it. If it is in use, a message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding a User

• Configuring a User

• Deleting a User

| Field | Description |
|---|---|
| Preferred CTI Device | This parameter comprises a dropdown list of the available devices controlled by the user. |
| Unity Connection Profile | This parameter comprises a dropdown list of the available Cisco Unity Connection profiles. If the list is empty, you may need to configure a Cisco Unity Connection profile for Cisco Unified Personal Communicator. |
| MeetingPlace Express Profile | This parameter comprises a dropdown list of the available Cisco MeetingPlace Express profiles. If the list is empty, you may need to configure a Cisco MeetingPlace Express profile for Cisco Unified Personal Communicator. |
| CTI Gateway Profile | This parameter comprises a dropdown list of the available Cisco CTI gateway profiles. If the list is empty, you may need to configure a Cisco CTI gateway profile for Cisco Unified Personal Communicator. |
| LDAP Profile | This parameter comprises a dropdown list of the available Cisco LDAP profiles. If the list is empty, you may need to configure a Cisco LDAP profile for Cisco Unified Personal Communicator. |
| SIP Proxy Profile | This parameter comprises a dropdown list of SIP proxy profiles and can be empty. |