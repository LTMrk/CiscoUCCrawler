---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b02servr-html-20dfcfae5a
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b02servr.html
retrieved_at: 2026-08-21T16:10:46.887667+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Server Configuration

## Chapter: Server Configuration

## Server Configuration

Use server configuration to specify the address of the server where Cisco Unified Presence Server is installed. If your network uses Domain Name System (DNS) services, you can specify the host name of the server. If your network does not use DNS services, you must specify the Internet Protocol (IP) address of the server.

Note You must update the DNS server with the appropriate Cisco Unified Presence Server name and address information before using that information to configure the Cisco Unified Presence Server.

For information about how to add, update, or delete a server address in the Cisco Unified Presence Server database, see the "Related Topics" section .

Note When you perform a fresh installation of Cisco Unified Presence Server, you must define any secondary servers (nodes) in the Cisco Unified Presence Server Administration Server Configuration window before you can install the Cisco Unified Presence Server software on a secondary server. To define a subsequent node, click Add New , as described in Step 1 above, and configure the server. After you add the secondary server, you can then install the Cisco Unified Presence Server software on that server.

## Finding a Server

Because you might have several servers in your network, Cisco Unified Presence Server lets you locate specific servers on the basis of specific criteria. Use the following procedure to locate servers.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose System > Server .

The Find and List Servers window displays. Use the two drop-down list boxes to search for a server.

Step 2 From the first Find Servers window drop-down list box, choose one of the following criteria:

• Host Name/IP Address

• Description

From the second Find Servers window drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 3 Specify the appropriate search text, if applicable, and click Find .

Tip To find all servers that are registered in the database, click Find without entering any search text.

A list of discovered servers displays by

• Host Name/IP Address

• Description

From the Find and List Servers window, you can also specify how many items per page to display.

Note You can delete multiple servers from the Find and List Servers window by checking the check boxes next to the appropriate servers and clicking Delete Selected . You can delete all servers in the window by checking the check box in the Matching records title bar and clicking Delete Selected .

Step 4 From the list of records, click the Server name that matches your search criteria.

The window displays the server that you choose.

Additional Information

See the "Related Topics" section .

## Configuring a Server

This section describes how to add or update a server address to the Cisco Unified Presence Server database.

Before You Begin

The following guideline applies to adding a server:

• Make sure that you add each server only once on the Server Configuration window. If you add a server by using the host name and add the same server by using the IP address, Cisco Unified Presence Server cannot accurately determine component versions for the server after a Cisco Unified Presence Server upgrade. If you have two entries in Cisco Unified Presence Server Administration for the same server, delete one of the entries before you upgrade (see the "Deleting a Server" section ).

Step 1 Perform one of the following tasks:

• To add a server, choose System > Server and click Add New .

• To update a server, find the server by using the procedure in the "Finding a Server" section .

The Server Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 2-1 .

Step 3 To save the data and to add the server to the database, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window)

Warning Changes to the server configuration do not take effect until you restart the Cisco Unified Presence Server proxy server. During the restart, the Cisco Enterprise SIP Proxy service drops any existing transactions and does not accept any new requests.

Step 4 Choose Cisco Unified Presence Server > Proxy Server > Settings .

The Proxy Configuration Settings window displays.

Step 5 Click Restart All Proxy Services .

Step 6 When confirmation window displays, click OK to restart all proxy services.

Additional Information

See the "Related Topics" section .

## Deleting a Server

This section describes how to delete a server from the Cisco Unified Presence Server database.

Before You Begin

If the dependency records feature is not enabled for the system, the dependency records summary window displays a message that shows the action that you can take to enable the dependency records; the message also displays information about high CPU consumption related to the dependency records feature.

Step 1 Find the server by using the procedure in the "Finding a Server" section .

Step 2 From list of matching records, choose the server that you want to delete.

Step 3 To delete the server, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

Warning Changes to the server configuration do not take effect until you restart the Cisco Unified Presence Server proxy server. During the restart, the Cisco Enterprise SIP Proxy service drops any existing transactions and does not accept any new requests.

Step 4 Choose Cisco Unified Presence Server > Proxy Server > Settings .

The Proxy Configuration Settings window displays.

Step 5 Click Restart All Proxy Services .

Step 6 When confirmation window displays, click OK to restart all proxy services.

Additional Information

See the "Related Topics" section .

## Server Configuration Settings

Table 2-1 describes the server configuration settings. For related procedures, see the "Related Topics" section .

Table 2-1 Server Configuration Settings

Host Name/ IP Address

If your network uses DNS services, you can enter the host name of the Cisco Unified Presence Server server. Otherwise, you must enter the full IP address of the server.

Note You must update the DNS server with the appropriate Cisco Unified Presence Server name and address information before using that information here.

MAC Address

For this optional entry, enter the media access control (MAC) address of the network interface card (NIC) in the Cisco Unified Presence Server server. The MAC address specifies the permanent hardware address of the NIC.

Description

For this optional entry, enter a description of the server.

## Related Topics

• Finding a Server

• Configuring a Server

• Deleting a Server

• Server Configuration Settings

| Server Information Field | Description |
|---|---|
| Host Name/ IP Address | If your network uses DNS services, you can enter the host name of the Cisco Unified Presence Server server. Otherwise, you must enter the full IP address of the server. Note You must update the DNS server with the appropriate Cisco Unified Presence Server name and address information before using that information here. |
| MAC Address | For this optional entry, enter the media access control (MAC) address of the network interface card (NIC) in the Cisco Unified Presence Server server. The MAC address specifies the permanent hardware address of the NIC. Tip If you plan to move the server periodically to different locations on the network, you must enter the MAC address, so other devices on the network can always identify the server. If you do not plan to relocate the server, consider entry of the MAC address as optional. |
| Description | For this optional entry, enter a description of the server. |