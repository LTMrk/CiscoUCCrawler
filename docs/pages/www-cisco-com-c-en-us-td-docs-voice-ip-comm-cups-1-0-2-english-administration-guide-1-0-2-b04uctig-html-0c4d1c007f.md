---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b04uctig-html-0c4d1c007f
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b04uctig.html
retrieved_at: 2026-08-21T16:12:39.999964+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: CTI Gateway Server

## Chapter: CTI Gateway Server

## CTI Gateway Server

Use CTI gateway server settings to configure settings that are related to CTI gateway. You can use this window to search for specific servers and change individual settings.

## Finding a CTI Gateway Server

Because you might have several CTI gateway servers in your network, Cisco Unified Presence Server lets you locate specific CTI gateway servers on the basis of specific criteria. Use the following procedure to locate specific CTI gateway servers.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Application > Unified Personal Communicator > CTI Gateway Server .

The Find and List CTI Gateway Hosts window displays. Use the two drop-down list boxes to search for CTI gateway hosts.

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

Tip To find all CTI gateway hosts that are registered in the database, click Find without entering any search text.

A list of discovered CTI gateway hosts displays.

Step 4 From the list of records, click the CTI gateway host that matches your search criteria.

The window displays the CTI gateway host that you choose.

Additional Information

See the "Related Topics" section .

## Configuring a CTI Gateway Server

This section describes how to add or update a CTI gateway server in the Cisco Unified Presence Server database.

Step 1 Perform one of the following tasks:

• To add a CTI gateway, choose Application > Unified Personal Communicator > CTI Gateway Server and click Add New .

• To update a CTI gateway host, find the host by using the procedure in the "Finding a CTI Gateway Server" section .

The CTI Gateway Host Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 29-1 .

Step 3 To save the data and to add the CTI gateway host to the database, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## CTI Gateway Server Configuration Settings

Table 29-1 describes the CTI gateway configuration parameters. For related procedures, see the "Related Topics" section .

Table 29-1 CTI Gateway Server Configuration Parameters

Name

This parameter specifies the name of the CTI gateway server.

Description

This parameter provides a general description of the CTI gateway server.

Hostname/IP Address

This parameter specifies the host name or IP address of the CTI gateway server.

Port

This parameter specifies the port number that is configured for the CTI gateway server.

Default: 2748

Protocol Type

This parameter specifies the protocol to use when the CTI gateway server is contacted. Choose one of the following values:

• TCP

• UDP

• TLS

Default: TCP

## Deleting a CTI Gateway Server

This section describes how to delete a CTI gateway server.

Step 1 Find the CTI gateway server by using the procedure in the "Finding a CTI Gateway Server" section .

Step 2 From list of matching records, choose the CTI gateway server that you want to delete.

Step 3 To delete the CTI gateway, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the CTI gateway server is not in use, Cisco Unified Presence Server deletes it. If it is in use, a message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding a CTI Gateway Server

• Configuring a CTI Gateway Server

• Deleting a CTI Gateway Server

| Field | Description |
|---|---|
| Name | This parameter specifies the name of the CTI gateway server. |
| Description | This parameter provides a general description of the CTI gateway server. |
| Hostname/IP Address | This parameter specifies the host name or IP address of the CTI gateway server. |
| Port | This parameter specifies the port number that is configured for the CTI gateway server. Default: 2748 |
| Protocol Type | This parameter specifies the protocol to use when the CTI gateway server is contacted. Choose one of the following values: • TCP • UDP • TLS Default: TCP |