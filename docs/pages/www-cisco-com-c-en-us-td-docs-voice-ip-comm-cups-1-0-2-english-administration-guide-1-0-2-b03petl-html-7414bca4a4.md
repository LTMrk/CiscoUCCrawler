---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b03petl-html-7414bca4a4
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b03petl.html
retrieved_at: 2026-08-21T16:11:41.046805+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Presence Engine Transport Listeners

## Chapter: Presence Engine Transport Listeners

## Presence Engine Transport Listeners

You can configure transport listeners for the SIP proxy server, presence engine, and profile agent. Each transport listener gets bound to a specific address and port combination. If you choose TLS protocol, you must also choose a TLS context.

## Finding Transport Listeners

Because you might have several transport listeners in your network, Cisco Unified Presence Server lets you locate specific transport listeners on the basis of specific criteria. Use the following procedure to locate transport listeners.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Unified Presence Server > Presence Engine > Transport Listeners .

The Find and List Transport Listeners window displays. Use the two drop-down list boxes to search for capabilities assignments.

Step 2 From the first Find Transport Listeners window drop-down list box, choose one of the following criteria:

• Name

• Port

From the second Find Transport Listeners window drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 3 Specify the appropriate search text, if applicable, and click Find .

Tip To find all transport listeners that are registered in the database, click Find without entering any search text.

A list of discovered transport listeners displays.

Step 4 From the list of records, click the transport listener that matches your search criteria.

The window displays the transport listener that you choose.

Additional Information

See the "Related Topics" section .

## Configuring a Transport Listener

This section describes how to add or update transport listeners in the Cisco Unified Presence Server database.

Step 1 Perform one of the following tasks:

• To add a transport listener, choose Unified Presence Server > Presence Engine > Transport Listeners and click Add New .

• To update a transport listener, find the transport listener by using the procedure in the "Finding Transport Listeners" section .

The Transport Listener Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 15-1 .

Note You must restart the SIP proxy server before any changes you make to the transport listeners take effect. To restart the proxy server, choose Cisco Unified Presence Server > Proxy Server > Settings . For more information, see Proxy Server Settings .

Step 3 To save the data, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## Transport Listener Configuration Settings

Table 15-1 describes the transport listener configuration settings. For related procedures, see the "Related Topics" section .

Table 15-1 Transport Listener Configuration Settings

Name

This parameter specifies the unique name of this transport listener.

Port

This parameter specifies the port number that is configured for this SIP transport.

Protocol Type

This parameter specifies what type of protocol this SIP transport will use, TCP, UDP, or TLS.

Service Type

This parameter specifies the service type of this transport listener:

• Cisco Proxy Server

• Cisco Presence

• Cisco Unified Client Profile Agent

TLS Context

This parameter specifies the TLS context that is associated with this transport listener and only applies when you choose the TLS protocol type.

Note The available TLS contexts get configured in the TLS Context Configuration window.

## Deleting a Transport Listener

This section describes how to delete a transport listener.

Step 1 Find the transport listener by using the procedure in the "Finding Transport Listeners" section .

Step 2 From list of matching records, choose the transport listener that you want to delete.

Note You must restart the SIP proxy server before any changes you make to the transport listeners take effect. To restart the proxy server, choose Cisco Unified Presence Server > Proxy Server > Settings . For more information, see Proxy Server Settings .

Step 3 To delete the transport listener, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the transport listener is not in use, Cisco Unified Presence Server deletes it. If it is in use, a message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding Transport Listeners

• Configuring a Transport Listener

• Deleting a Transport Listener

| Field | Description |
|---|---|
| Name | This parameter specifies the unique name of this transport listener. |
| Port | This parameter specifies the port number that is configured for this SIP transport. |
| Protocol Type | This parameter specifies what type of protocol this SIP transport will use, TCP, UDP, or TLS. |
| Service Type | This parameter specifies the service type of this transport listener: • Cisco Proxy Server • Cisco Presence • Cisco Unified Client Profile Agent |
| TLS Context | This parameter specifies the TLS context that is associated with this transport listener and only applies when you choose the TLS protocol type. Note The available TLS contexts get configured in the TLS Context Configuration window. |