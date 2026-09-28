---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b04umps-html-18fb648274
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b04umps.html
retrieved_at: 2026-08-21T16:12:31.201189+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: MeetingPlace Server

## Chapter: MeetingPlace Server

## MeetingPlace Express Server

Use Cisco MeetingPlace Express Server settings to configure settings that relate to Cisco MeetingPlace Express. You can use this window to search for specific servers and change individual settings.

## Finding a Cisco MeetingPlace Express Server

Because you might have several Cisco MeetingPlace Express servers in your network, Cisco Unified Presence Server lets you locate specific Cisco MeetingPlace servers on the basis of specific criteria. Use the following procedure to locate specific Cisco MeetingPlace Express servers.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Application > Unified Personal Communicator > MeetingPlace Express Server .

The Find and List MeetingPlace Express Hosts window displays. Use the two drop-down list boxes to search for Cisco MeetingPlace Express hosts.

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

Tip To find all Cisco MeetingPlace Express hosts that are registered in the database, click Find without entering any search text.

A list of discovered Cisco MeetingPlace Express hosts displays.

Step 4 From the list of records, click the Cisco MeetingPlace Express host that matches your search criteria.

The window displays the Cisco MeetingPlace Express host that you choose.

Additional Information

See the "Related Topics" section .

## Configuring a Cisco MeetingPlace Express Server

This section describes how to add or update a Cisco MeetingPlace Express host in the Cisco Unified Presence Server database.

Step 1 Perform one of the following tasks:

• To add a Cisco MeetingPlace Express server, choose Application > Unified Personal Communicator > MeetingPlace Express Server and click Add New .

• To update a Cisco MeetingPlace Express server, find the host by using the procedure in the "Finding a Cisco MeetingPlace Express Server" section .

The MeetingPlace Express Host Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 27-1 .

Step 3 To save the data and to add the Cisco MeetingPlace Express server to the database, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## Cisco MeetingPlace Express Server Configuration Settings

Table 27-1 describes the Cisco MeetingPlace Express Server configuration parameters. For related procedures, see the "Related Topics" section .

Table 27-1 Cisco MeetingPlace Express Server Configuration Parameters

Name

The parameter specifies the name of the Cisco MeetingPlace Express server.

Maximum characters: 128

Description

This parameter provides a general description of the Cisco MeetingPlace Express server.

Maximum characters: 128

Hostname/IP Address

This parameter specifies the host name or IP address of the Cisco MeetingPlace Express server.

Port

This parameter specifies the port number that is configured for the Cisco MeetingPlace Express server.

Default: 80

Protocol Type

This parameter specifies the protocol to use when contacting the Cisco MeetingPlace Express server. Choose one of the following values:

• HTTP

• HTTPS

Default: HTTP

## Deleting a Cisco MeetingPlace Express Server

This section describes how to delete a Cisco MeetingPlace Express server.

Step 1 Find the Cisco MeetingPlace Express server by using the procedure in the "Finding a Cisco MeetingPlace Express Server" section .

Step 2 From list of matching records, choose the Cisco MeetingPlace Express server that you want to delete.

Step 3 To delete the Cisco MeetingPlace Express server, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the Cisco MeetingPlace Express server is not in use, Cisco Unified Presence Server deletes it. If it is in use, a message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding a Cisco MeetingPlace Express Server

• Configuring a Cisco MeetingPlace Express Server

• Deleting a Cisco MeetingPlace Express Server

| Field | Description |
|---|---|
| Name | The parameter specifies the name of the Cisco MeetingPlace Express server. Maximum characters: 128 |
| Description | This parameter provides a general description of the Cisco MeetingPlace Express server. Maximum characters: 128 |
| Hostname/IP Address | This parameter specifies the host name or IP address of the Cisco MeetingPlace Express server. |
| Port | This parameter specifies the port number that is configured for the Cisco MeetingPlace Express server. Default: 80 |
| Protocol Type | This parameter specifies the protocol to use when contacting the Cisco MeetingPlace Express server. Choose one of the following values: • HTTP • HTTPS Default: HTTP |