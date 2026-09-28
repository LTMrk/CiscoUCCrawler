---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b04usrv-html-52400f52f2
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b04usrv.html
retrieved_at: 2026-08-21T16:12:22.963820+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Unity Server

## Chapter: Unity Server

## Unity Connection Server

Use Cisco Unity Connection Server settings to configure settings that are related to Cisco Unity Connection. You can use this window to search for specific servers and change individual settings.

## Finding a Cisco Unity Connection Server

Because you might have several Cisco Unity Connection Servers in your network, Cisco Unified Presence Server lets you locate specific Cisco Unity Connection servers on the basis of specific criteria.

Use the following procedure to locate specific Cisco Unity Connection servers.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Application > Unified Personal Communicator > Unity Connection Server .

The Find and List Unity Connections Hosts window displays. Use the two drop-down list boxes to search for Cisco Unity Connection hosts.

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

Tip To find all Cisco Unity Connection hosts that are registered in the database, click Find without entering any search text.

A list of discovered Cisco Unity Connection hosts displays.

Step 4 From the list of records, click the Cisco Unity Connection host that matches your search criteria.

The window displays the Cisco Unity Connection host that you choose.

Additional Information

See the "Related Topics" section .

## Configuring a Cisco Unity Connection Host

This section describes how to add or update a Cisco Unity Connection host in the Cisco Unified Presence Server database.

Step 1 Perform one of the following tasks:

• To add a user, choose Application > Unified Personal Communicator > Unity Connection Server and click Add New .

• To update a Cisco Unity Connection host, find the host by using the procedure in the "Finding a Cisco Unity Connection Server" section .

The Unity Connection Host Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 25-1 .

Step 3 To save the data and to add the Cisco Unity Connection host to the database, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## Cisco Unity Connection Server Configuration Settings

Table 25-1 describes the user settings configuration parameters. For related procedures, see the "Related Topics" section .

Table 25-1 Cisco Unity Connection Server Configuration Parameters

Name

This parameter specifies the name of the Cisco Unity Connection host.

Maximum characters: 128

Description

This parameter provides a general description of the Cisco Unity Connection server.

Hostname/IP Address

This parameter specifies the host name or IP Address of the Cisco Unity Connection server.

Port

This parameter specifies the port number that is configured for the Cisco Unity Connection server.

Default: 143

Protocol Type

This parameter specifies the protocol to use when contacting the Cisco Unity Connection server. Choose one of the following values:

• TCP

• UDP

• TLS

Default: TCP

## Deleting a Cisco Unity Connection Server

This section describes how to delete a Cisco Unity Connection server.

Step 1 Find the user by using the procedure in the "Finding a Cisco Unity Connection Server" section .

Step 2 From list of matching records, choose the Cisco Unity Connection server that you want to delete.

Step 3 To delete the Cisco Unity Connection server, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the Cisco Unity Connection server is not in use, Cisco Unified Presence Server deletes it. If it is in use, a message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding a Cisco Unity Connection Server

• Configuring a Cisco Unity Connection Host

• Deleting a Cisco Unity Connection Server

| Field | Description |
|---|---|
| Name | This parameter specifies the name of the Cisco Unity Connection host. Maximum characters: 128 |
| Description | This parameter provides a general description of the Cisco Unity Connection server. |
| Hostname/IP Address | This parameter specifies the host name or IP Address of the Cisco Unity Connection server. |
| Port | This parameter specifies the port number that is configured for the Cisco Unity Connection server. Default: 143 |
| Protocol Type | This parameter specifies the protocol to use when contacting the Cisco Unity Connection server. Choose one of the following values: • TCP • UDP • TLS Default: TCP |