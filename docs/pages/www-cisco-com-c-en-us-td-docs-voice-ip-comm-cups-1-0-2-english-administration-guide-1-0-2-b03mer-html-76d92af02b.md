---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b03mer-html-76d92af02b
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b03mer.html
retrieved_at: 2026-08-21T16:11:20.623502+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Method/Event Routing

## Chapter: Method/Event Routing

## Method/Event Routing

Use method-based or event-based routing to configure the SIP proxy server to route SIP messages on the basis of their content.

## Finding Method/Event Routes

Because you might have several method-based or event-based routes in your network, Cisco Unified Presence Server lets you locate specific method-based or event-based routes on the basis of specific criteria. Use the following procedure to locate method/event routes.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Unified Presence Server > Proxy Server>Method/Event Routing .

The Find and List Method/Event-Based Routing Entries window displays. To search for method/event routes, use the two drop-down list boxes.

Step 2 From the first Find Method/Event-Based Routing window drop-down list box, choose one of the following criteria:

• Name

• Description

• Content Token

• Destination Address

• Destination Port

From the second Find Servers window drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 3 Specify the appropriate search text, if applicable, and click Find .

Tip To find all method-based or event-based routes that are registered in the database, click Find without entering any search text.

A list of discovered method-based or event-based routes displays.

Step 4 From the list of records, click the route that matches your search criteria.

The window displays the route that you choose.

Additional Information

See the "Related Topics" section .

## Configuring a Method-based or Event-based Route

This section describes how to add or update method-based or event-based routes in the Cisco Unified Presence Server database.

Step 1 Perform one of the following tasks:

• To add a method/event route, choose Unified Presence Server > Proxy Server>Method/Event Routing and click Add New .

• To update a method-based or event-based route, find the route by using the procedure in the "Finding Method/Event Routes" section .

The Method/Event-Based Routing Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 10-1 .

Step 3 To save the data and to add the server to the database, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## Method/Event Route Configuration Settings

Table 10-1 describes the Method/Event route configuration settings. For related procedures, see the "Related Topics" section .

Table 10-1 Method/Event Route Configuration Settings

Name

This parameter specifies the name that is associated with this particular method/event route.

Description

This parameter specifies the description of a particular method/event route.

Current Token

This parameter specifies the content search string that will be used to route a SIP message.

Examples include PUBLISH and SUBSCRIBE.

Content Category

This parameter specifies the content category, either method-based or event-based.

Destination Address

This parameter specifies the domain name or IP address of the destination (next hop) where the SIP message will be sent.

Destination Port

This parameter specifies the port number of the destination (next hop).

Default port: 5060

Protocol Type

This parameter specifies the protocol type that will be used when the SIP message is forwarded, TCP, UDP, or TLS.

## Deleting a Method/Event Route

This section describes how to delete a method-based or event-based route.

Step 1 Find the method/event route by using the procedure in the "Finding Method/Event Routes" section .

Step 2 From list of matching records, choose the route that you want to delete.

Step 3 To delete the route, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the method/event route is not in use, Cisco Unified Presence Server deletes it. If it is in use, an error message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding Method/Event Routes

• Configuring a Method-based or Event-based Route

• Deleting a Method/Event Route

| Field | Description |
|---|---|
| Name | This parameter specifies the name that is associated with this particular method/event route. |
| Description | This parameter specifies the description of a particular method/event route. |
| Current Token | This parameter specifies the content search string that will be used to route a SIP message. Examples include PUBLISH and SUBSCRIBE. |
| Content Category | This parameter specifies the content category, either method-based or event-based. |
| Destination Address | This parameter specifies the domain name or IP address of the destination (next hop) where the SIP message will be sent. |
| Destination Port | This parameter specifies the port number of the destination (next hop). Default port: 5060 |
| Protocol Type | This parameter specifies the protocol type that will be used when the SIP message is forwarded, TCP, UDP, or TLS. |