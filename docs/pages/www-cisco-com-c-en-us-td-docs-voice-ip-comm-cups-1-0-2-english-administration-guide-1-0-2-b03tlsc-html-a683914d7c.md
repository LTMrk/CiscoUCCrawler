---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b03tlsc-html-a683914d7c
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b03tlsc.html
retrieved_at: 2026-08-21T16:11:45.223450+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: TLS Context Configuration

## Chapter: TLS Context Configuration

## TLS Context Configuration

Each transport listener can have a single associated transport layer security (TLS) context, and each TLS context can have multiple ciphers and peer subjects.

TLS context configuration enables you to map ciphers and peer subjects to a transport listener.

## Finding TLS Contexts

Because you might have several TLS contexts in your network, Cisco Unified Presence Server lets you locate specific TLS contexts on the basis of specific criteria. Use the following procedure to locate TLS contexts.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Unified Presence Server > Security > TLS Context Configuration .

The Find and List TLS Contexts window displays. Use the drop-down list box to search for TLS contexts.

Step 2 From the Find TLS Context window Name drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 3 Specify the appropriate search text, if applicable, and click Find .

Tip To find all TLS contexts that are registered in the database, click Find without entering any search text.

A list of discovered TLS contexts displays.

Step 4 From the list of records, click the TLS context that matches your search criteria.

The window displays the TLS context that you choose.

Additional Information

See the "Related Topics" section .

## Configuring a TLS Context

This section describes how to add or update TLS contexts in the Cisco Unified Presence Server database.

Step 1 Perform one of the following tasks:

• To add a TLS context, choose Unified Presence Server > Security > TLS Context Configuration and click Add New .

• To update a TLS context, find the TLS context by using the procedure in the "Finding TLS Contexts" section .

The TLS Context Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 16-1 .

Step 3 To choose the appropriate TLS cipher, click the up or down arrow.

Step 4 To choose the appropriate TLS peer subject, click the up or down arrow.

Note You must restart the SIP proxy server before any changes you make to the TLS context take effect. To restart the proxy server, choose Cisco Unified Presence Server > Proxy Server > Settings . For more information, see Proxy Server Settings .

Step 5 To save the data, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## TLS Context Configuration Settings

Table 16-1 describes the TLS context configuration settings. For related procedures, see the "Related Topics" section .

Table 16-1 TLS Context Configuration Settings

Name

This parameter specifies the unique name of the associated transport listener.

Description

This parameter specifies a description of this TLS context.

Authorization Policy

This parameter specifies the authorization type for this particular TLS context. From the drop-down list, choose either Server or Peer (default).

TLS Cipher Mapping

These fields display the available and selected TLS ciphers.

TLS Peer Subject Mapping

These fields display the available and selected TLS peer subjects.

Note You can define TLS peer subjects in the TLS Peer Subjects window.

## Deleting a TLS Context

This section describes how to delete a TLS context.

Step 1 Find the TLS context by using the procedure in the "Finding TLS Contexts" section .

Step 2 From list of matching records, choose the TLS context that you want to delete.

Note You must restart the SIP proxy server before any changes you make to the TLS context take effect. To restart the proxy server, choose Cisco Unified Presence Server > Proxy Server > Settings . For more information, see Proxy Server Settings .

Step 3 To delete the TLS context, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the TLS context is not in use, Cisco Unified Presence Server deletes it. If it is in use, a message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding TLS Contexts

• Configuring a TLS Context

• Deleting a TLS Context

| Field | Description |
|---|---|
| Name | This parameter specifies the unique name of the associated transport listener. |
| Description | This parameter specifies a description of this TLS context. |
| Authorization Policy | This parameter specifies the authorization type for this particular TLS context. From the drop-down list, choose either Server or Peer (default). |
| TLS Cipher Mapping | These fields display the available and selected TLS ciphers. |
| TLS Peer Subject Mapping | These fields display the available and selected TLS peer subjects. Note You can define TLS peer subjects in the TLS Peer Subjects window. |