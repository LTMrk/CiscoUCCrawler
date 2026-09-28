---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b03tlsp-html-a5263c7029
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b03tlsp.html
retrieved_at: 2026-08-21T16:11:49.355930+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: TLS Peer Subjects

## Chapter: TLS Peer Subjects

## TLS Peer Subjects

TLS peer subject configuration enables you to create and modify peer subjects that you can associate to a transport listener.

## Finding TLS Peer Subjects

Because you might have several TLS peer subjects in your network, Cisco Unified Presence Server lets you locate specific TLS peer subjects on the basis of specific criteria. Use the following procedure to locate TLS peer subjects.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Unified Presence Server > Security > TLS Peer Subjects .

The Find and List TLS Peer Subjects window displays. Use the drop-down list box to search for TLS peer subjects.

Step 2 From the first Find TLS Peer Subjects window drop-down list box, choose one of the following criteria:

• Peer Subject Name

• Description

From the second Find TLS Peer Subjects window drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 3 Specify the appropriate search text, if applicable, and click Find .

Tip To find all TLS peer subjects that are registered in the database, click Find without entering any search text.

A list of discovered TLS peer subjects displays.

Step 4 From the list of records, click the TLS peer subject that matches your search criteria.

The window displays the TLS peer subject that you choose.

Additional Information

See the "Related Topics" section .

## Configuring a TLS Peer Subject

This section describes how to add or update TLS peer subjects in the Cisco Unified Presence Server database.

Step 1 Perform one of the following tasks:

• To add a TLS peer subject, choose Unified Presence Server > Security > TLS Peer Subjects and click Add New .

• To update a TLS peer subject, find the TLS peer subject by using the procedure in the "Finding TLS Peer Subjects" section .

The TLS Peer Subject Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 17-1 .

Note You must restart the SIP proxy server before any changes you make to TLS peer subjects take effect. To restart the proxy server, choose Cisco Unified Presence Server > Proxy Server > Settings . For more information, see Proxy Server Settings .

Step 3 To save the data, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## TLS Peer Subject Configuration Settings

Table 17-1 describes the TLS peer subject configuration settings. For related procedures, see the "Related Topics" section .

Table 17-1 TLS Peer Subject Configuration Settings

Peer Subject Name

This parameter specifies the unique name of the TLS peer subject.

Description

This parameter specifies a description of this TLS peer subject.

## Deleting a TLS Peer Subject

This section describes how to delete a TLS peer subject.

Step 1 Find the TLS peer subject by using the procedure in the "Finding TLS Peer Subjects" section .

Step 2 From list of matching records, choose the TLS peer subject that you want to delete.

Note You must restart the SIP proxy server before any changes you make to TLS peer subjects take effect. To restart the proxy server, choose Cisco Unified Presence Server > Proxy Server > Settings . For more information, see Proxy Server Settings .

Step 3 To delete the TLS peer subject, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the TLS peer subject is not in use, Cisco Unified Presence Server deletes it. If it is in use, a message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding TLS Peer Subjects

• Configuring a TLS Peer Subject

• Deleting a TLS Peer Subject

| Field | Description |
|---|---|
| Peer Subject Name | This parameter specifies the unique name of the TLS peer subject. |
| Description | This parameter specifies a description of this TLS peer subject. |