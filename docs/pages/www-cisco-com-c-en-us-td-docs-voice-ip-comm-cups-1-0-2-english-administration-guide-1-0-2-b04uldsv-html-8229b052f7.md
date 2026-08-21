---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b04uldsv-html-8229b052f7
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b04uldsv.html
retrieved_at: 2026-08-21T16:12:48.091887+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: LDAP Server

## Chapter: LDAP Server

## LDAP Server

Use LDAP server settings to configure settings that are related to the LDAP server. You can use this window to search for specific servers and change individual settings.

## Finding an LDAP Server

Because you might have several LDAP servers in your network, Cisco Unified Presence Server lets you locate specific LDAP servers on the basis of specific criteria. Use the following procedure to locate specific LDAP servers.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Application > Unified Personal Communicator > LDAP Server .

The Find and List LDAP Hosts window displays. Use the two drop-down list boxes to search for LDAP hosts.

Step 2 From the first drop-down list box, choose one of the following criteria:

• Name

• Description

• Hostname/IP Address

• Port

From the second drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 3 Specify the appropriate search text, if applicable, and click Find .

Tip To find all LDAP hosts that are registered in the database, click Find without entering any search text.

A list of discovered LDAP hosts displays.

Step 4 From the list of records, click the LDAP host that matches your search criteria.

The window displays the LDAP host that you choose.

Additional Information

See the "Related Topics" section .

## Configuring an LDAP Server

This section describes how to add or update an LDAP host in the Cisco Unified Presence Server database.

Step 1 Perform one of the following tasks:

• To add an LDAP server, choose Application > Unified Personal Communicator > LDAP Server and click Add New .

• To update an LDAP host, find the host by using the procedure in the "Finding an LDAP Server" section .

The LDAP Host Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 31-1 .

Step 3 To save the data and to add the LDAP host to the database, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## LDAP Server Configuration Settings

Table 31-1 describes the LDAP settings configuration parameters. For related procedures, see the "Related Topics" section .

Table 31-1 LDAP Server Configuration Parameters

Name

This parameter specifies the name of the LDAP server.

Description

This parameter provides a general description of the LDAP server.

Hostname/IP Address

This parameter specifies the host name or IP address of the LDAP server.

Port

This parameter specifies the port number that is configured for the LDAP server.

Protocol Type

This parameter specifies the protocol to use when the LDAP server is contacted. Choose one of the following values:

• TCP

• UDP

• TLS

## Deleting an LDAP Server

This section describes how to delete an LDAP server.

Step 1 Find the LDAP server by using the procedure in the "Finding an LDAP Server" section .

Step 2 From list of matching records, choose the LDAP server that you want to delete.

Step 3 To delete the LDAP server, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the LDAP server is not in use, Cisco Unified Presence Server deletes it. If it is in use, a message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding an LDAP Server

• Configuring an LDAP Server

• Deleting an LDAP Server

| Field | Description |
|---|---|
| Name | This parameter specifies the name of the LDAP server. |
| Description | This parameter provides a general description of the LDAP server. |
| Hostname/IP Address | This parameter specifies the host name or IP address of the LDAP server. |
| Port | This parameter specifies the port number that is configured for the LDAP server. |
| Protocol Type | This parameter specifies the protocol to use when the LDAP server is contacted. Choose one of the following values: • TCP • UDP • TLS |