---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b04uldpr-html-e91b84d384
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b04uldpr.html
retrieved_at: 2026-08-21T16:12:52.358518+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: LDAP Profile

## Chapter: LDAP Profile

## LDAP Profile

Use LDAP Profile settings to configure LDAP directory information, LDAP search context information, LDAP server information, and the users that are associated with the profile. You can use this window to search for specific profiles and change individual settings.

## Finding an LDAP Profile

Because you might have several LDAP profiles in your network, Cisco Unified Presence Server lets you locate specific LDAP profiles on the basis of specific criteria. Use the following procedure to locate specific LDAP profiles.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Application > Unified Personal Communicator > LDAP Profile .

The Find and List LDAP Profiles window displays. Use the drop-down list boxes to search for LDAP profiles.

Step 2 From the first drop-down list box, choose one of the following criteria:

• Name

• Description

Step 3 From the first drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 4 Specify the appropriate search text, if applicable, and click Find .

Tip To find all LDAP profiles that are registered in the database, click Find without entering any search text.

A list of discovered LDAP profiles displays.

Step 5 From the list of records, click the LDAP profile that matches your search criteria.

The window displays the LDAP profile that you choose.

Additional Information

See the "Related Topics" section .

## Configuring an LDAP Profile

This section describes how to add or update an LDAP profile in the Cisco Unified Presence Server database.

Step 1 Perform one of the following tasks:

• To add an LDAP profile, choose Application > Unified Personal Communicator > LDAP Profile and click Add New .

• To update an LDAP profile, find the profile by using the procedure in the "Finding an LDAP Profile" section .

The LDAP Profile Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 32-1 .

Step 3 To allow users to log in anonymously with read-only access, click the Anonymous Bind check box.

Step 4 To perform a recursive search of the directory starting at the search base, choose Recursive Search.

Step 5 To associate users with the LDAP profile, click Add Users to Profile .

The Find and List Users window displays.

Step 6 From the first drop-down list box, choose one of the following criteria:

• First name

• Middle name

• Last name

• User ID

• Department

Step 7 From the second drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 8 Specify the appropriate search text, if applicable, and click Find .

Tip To find all users that are registered in the database, click Find without entering any search text.

A list of discovered users displays.

Step 9 From the list of records, click the users that you want to add to the LDAP profile or click Select All .

Step 10 To add the users to the LDAP profile, click Add Selected .

Step 11 To exit the Find and List Users window, Click Close .

Step 12 To save the data and to add the LDAP profile to the database profile, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## LDAP Profile Configuration Settings

Table 32-1 describes the LDAP profile configuration parameters. For related procedures, see the "Related Topics" section .

Table 32-1 LDAP Profile Configuration Parameters

Name

This parameter specifies the name of the LDAP profile.

Maximum characters: 128

Description

This parameter provides a general description of the LDAP profile.

Maximum characters: 128

Bind Distinguished Name (DN)

This parameter specifies the administrator-level account information in the form useraccount@domain.com . This is the distinguished name with which you bind for authenticated bind.

Maximum characters: 128

Password

This parameter specifies the password for the LDAP manager user name.

Maximum characters: 128

Confirm Password

Confirm the password for the LDAP manager user name.

Maximum characters: 128

Anonymous Bind checkbox

Choose Anonymous Bind so users can log in anonymously to this LDAP server for read-only access. To use the user credentials to log in to this LDAP server, clear this check box.

Search Context

This parameter specifies the location where all LDAP users exist, either a container or directory.

Maximum characters: 128

Recursive Search checkbox

To perform a recursive search of the directory starting at the search base, choose Recursive Search.

Primary LDAP Server

This parameter specifies the primary LDAP server. From the dropdown list, you can choose from the LDAP servers that you have already defined on the system.

Backup LDAP Server

This parameter specifies the backup LDAP server. From the dropdown list, you can choose from the LDAP servers that you have already defined on the system. You can specify two backup LDAP servers.

## Deleting an LDAP Profile

This section describes how to delete an LDAP profile.

Step 1 Find the LDAP profile by using the procedure in the "Finding an LDAP Profile" section .

Step 2 From list of matching records, choose the LDAP profile that you want to delete.

Step 3 To delete the profile, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the LDAP profile is not in use, Cisco Unified Presence Server deletes it. If it is in use, a message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding an LDAP Profile

• Configuring an LDAP Profile

• Deleting an LDAP Profile

| Field | Description |
|---|---|
| LDAP Profile Information |
| Name | This parameter specifies the name of the LDAP profile. Maximum characters: 128 |
| Description | This parameter provides a general description of the LDAP profile. Maximum characters: 128 |
| LDAP Directory Information |
| Bind Distinguished Name (DN) | This parameter specifies the administrator-level account information in the form useraccount@domain.com . This is the distinguished name with which you bind for authenticated bind. Maximum characters: 128 |
| Password | This parameter specifies the password for the LDAP manager user name. Maximum characters: 128 |
| Confirm Password | Confirm the password for the LDAP manager user name. Maximum characters: 128 |
| Anonymous Bind checkbox | Choose Anonymous Bind so users can log in anonymously to this LDAP server for read-only access. To use the user credentials to log in to this LDAP server, clear this check box. |
| LDAP Search Context Information |
| Search Context | This parameter specifies the location where all LDAP users exist, either a container or directory. Maximum characters: 128 |
| Recursive Search checkbox | To perform a recursive search of the directory starting at the search base, choose Recursive Search. |
| LDAP Server Information |
| Primary LDAP Server | This parameter specifies the primary LDAP server. From the dropdown list, you can choose from the LDAP servers that you have already defined on the system. |
| Backup LDAP Server | This parameter specifies the backup LDAP server. From the dropdown list, you can choose from the LDAP servers that you have already defined on the system. You can specify two backup LDAP servers. |