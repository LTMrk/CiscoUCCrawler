---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b03bgtw-html-6ec9bb6d05
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b03bgtw.html
retrieved_at: 2026-08-21T16:11:36.856221+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Presence Engine Backend Gateways

## Chapter: Presence Engine Backend Gateways

## CallManager Presence Gateways

Use the presence gateways window to configure the gateways that the presence engine must know about to receive presence information.

## Finding Presence Gateways

Because you might have several presence gateways in your network, Cisco Unified Presence Server lets you locate specific gateways on the basis of specific criteria. Use the following procedure to locate presence gateways.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Unified Presence Server > Presence Engine > CallManager Presence Gateways .

The Find and List CallManager Presence Gateways window displays. Use the drop-down list box to search for presence gateways.

Step 2 From the drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 3 Specify the appropriate search text, if applicable, and click Find .

Tip To find all presence gateways that are registered in the database, click Find without entering any search text.

A list of discovered presence gateways displays.

Step 4 From the list of records, click the presence gateway that matches your search criteria.

The window displays the presence gateway that you choose.

Additional Information

See the "Related Topics" section .

## Configuring a Presence Gateway

This section describes how to add or update presence gateways in the Cisco Unified Presence Server database.

Step 1 Perform one of the following tasks:

• To add a presence gateway, choose Unified Presence Server > Presence Engine > CallManager Presence Gateways and click Add New .

• To update a presence gateway, find the presence gateway by using the procedure in the "Finding Presence Gateways" section .

The CallManager Presence Gateway Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 14-1 .

Step 3 To save the data, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## Presence Gateway Configuration Settings

Table 14-1 describes the presence gateway configuration settings. For related procedures, see the "Related Topics" section .

Table 14-1 Presence Gateway Configuration Settings

Description

This parameter specifies the description of this presence gateway.

Maximum characters: 255

CallManager Presence Gateway

This parameter specifies the fully qualified domain name or the IP address of the associated Cisco Unified Callmanager server.

## Deleting a Presence Gateway

This section describes how to delete a presence gateway.

Step 1 Find the gateway by using the procedure in the "Finding Presence Gateways" section .

Step 2 From list of matching records, choose the gateway that you want to delete.

Step 3 To delete the gateway, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the gateway is not in use, Cisco Unified Presence Server deletes it. If it is in use, a message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding Presence Gateways

• Configuring a Presence Gateway

• Deleting a Presence Gateway

| Field | Description |
|---|---|
| Description | This parameter specifies the description of this presence gateway. Maximum characters: 255 |
| CallManager Presence Gateway | This parameter specifies the fully qualified domain name or the IP address of the associated Cisco Unified Callmanager server. |