---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b03iacl-html-926e8feb30
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b03iacl.html
retrieved_at: 2026-08-21T16:11:28.748857+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Incoming ACL

## Chapter: Incoming ACL

## Incoming ACL

In the Access Control List (ACL), you can configure patterns that control which hosts and domains can access Cisco Unified Presence Server.

## Finding Incoming ACL Entries

Because you might have several ACL entries your network, Cisco Unified Presence Server lets you locate specific incoming ACL entries on the basis of specific criteria. Use the following procedure to locate ACL entries.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Unified Presence Server > Proxy Server > Incoming ACL .

The Find and List Allowed Incoming Hosts window displays. Use the drop-down list box to search for ACL entries.

Step 2 From the drop-down list box, choose one of the following criteria for the address pattern:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 3 Specify the appropriate search text, if applicable, and click Find .

Tip To find all ACL entries that are registered in the database, click Find without entering any search text.

A list of discovered ACL entries displays.

Step 4 From the list of records, click the ACL entry that matches your search criteria.

The window displays the ACL entry that you choose.

Additional Information

See the "Related Topics" section .

## Configuring Incoming ACL

This section describes how to add or update incoming ACL information in the Cisco Unified Presence Server database.

Step 1 Perform one of the following tasks:

• To add an incoming ACL entry, choose Unified Presence Server > Proxy Server>Incoming ACL and click Add New .

• To update an incoming ACL entry, find the ACL entry by using the procedure in the "Finding Incoming ACL Entries" section .

The Proxy Access Control List Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 12-1 .

Step 3 To save the data, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## Incoming ACL Configuration Settings

Table 12-1 describes the incoming ACL configuration settings. For related procedures, see the "Related Topics" section .

Table 12-1 Incoming ACL Configuration Settings

Description

This parameter specifies a general description of the ACL entry.

Address Pattern

This parameter specifies the address or pattern of the incoming host or domain as either an IP address or a fully qualified domain name.

## Deleting an Incoming ACL Entry

This section describes how to delete an incoming ACL entry.

Step 1 Find the ACL entry by using the procedure in the "Finding Incoming ACL Entries" section .

Step 2 From list of matching records, choose the ACL entry that you want to delete.

Step 3 To delete the ACL entry, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the ACL entry is not in use, Cisco Unified Presence Server deletes it. If it is in use, a message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding Incoming ACL Entries

• Configuring Incoming ACL

• Deleting an Incoming ACL Entry

| Field | Description |
|---|---|
| Description | This parameter specifies a general description of the ACL entry. |
| Address Pattern | This parameter specifies the address or pattern of the incoming host or domain as either an IP address or a fully qualified domain name. |