---
doc_id: www-cisco-com-c-en-us-td-docs-voice-ip-comm-cups-1-0-2-english-administration-guide-1-0-2-b03statr-html-f017097869
source_url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cups/1_0_2/english/administration/guide/1_0_2/b03statr.html
retrieved_at: 2026-08-21T16:11:16.363749+00:00
---

Cisco Unified Presence Server Administration Guide, Release 1.0(2)

# Cisco Unified Presence Server Administration Guide, Release 1.0(2)

Updated: August 28, 2006

Chapter: Static Routes

## Chapter: Static Routes

## Static Routes

Use static routes to configure a static route that the SIP proxy server uses. A dynamic route represents a path through the network that gets automatically calculated according to routing protocols and routing update messages. A static route represents a fixed path through the network that you explicitly configure. Static routes take precedence over dynamic routes.

## Finding Static Routes

Because you might have several static routes in your network, Cisco Unified Presence Server lets you locate specific static routes on the basis of specific criteria. Use the following procedure to locate static routes.

Note During your work in a browser session, the cookies on the client machine store your find/list search preferences. If you navigate to other menu items and return to this menu item, or if you close the browser and then open a new browser window, the system retains your Cisco Unified Presence Server search preferences until you modify your search.

Step 1 Choose Unified Presence Server > Proxy Server > Static Routes .

The Find and List Static Routes window displays. Use the two drop-down list boxes to search for capabilities assignments.

Step 2 From the first Find Static Routes window drop-down list box, choose one of the following criteria:

• Destination Pattern

• Description

• Next Hop

• Priority

• Weight

From the second Find Servers window drop-down list box, choose one of the following criteria:

• begins with

• contains

• is exactly

• ends with

• is empty

• is not empty

Step 3 Specify the appropriate search text, if applicable, and click Find .

Tip To find all static routes that are registered in the database, click Find without entering any search text.

A list of discovered static routes displays.

Step 4 From the list of records, click the static route that matches your search criteria.

The window displays the static route that you choose.

Additional Information

See the "Related Topics" section .

## Configuring Static Routes

This section describes how to add or update static routes in the Cisco Unified Presence Server database.

Step 1 Perform one of the following tasks:

• To add a static route, choose Unified Presence Server > Proxy Server > Static Routes and click Add New .

• To update a server, find the server by using the procedure in the "Finding Static Routes" section .

The Static Route Configuration window displays.

Step 2 Enter the appropriate settings as described in Table 9-1 .

Step 3 To save the data and to add the server to the database, click the Save icon that displays in the tool bar in the upper, left corner of the window (or click the Save button that displays at the bottom of the window).

Additional Information

See the "Related Topics" section .

## Static Route Configuration Settings

Table 9-1 describes the static route configuration settings. For related procedures, see the "Related Topics" section .

Table 9-1 Static Route Configuration Settings

Destination Pattern

This field specifies the pattern of the incoming number.

You can use "." as a wildcard for a single character and "*" as wildcard as a wildcard for multiple characters.

A dash or hyphen, "-", is also allowed anywhere in the pattern

Wildcard Usage

For phones

• A dot can exist anywhere in the pattern.

• An asterisk can only exist at the end.

For IP addresses and host names

• An asterisk can be used as part of the a host name.

• The dot acts as a literal value in a host name.

An escaped asterisk sequence, \*, matches a literal * and can exist anywhere.

Description

This parameter specifies the description of a particular static route.

Next Hop

This parameter specifies the domain name or IP address of the destination (next hop) and can be specified as either a fully qualified domain name (FQDN) or dotted IP address.

Next Hop Port

This parameter specifies the port number of the destination (next hop).

Default: 5060

Route Type

This parameter specifies the route type, User or Domain.

Protocol Type

This parameter specifies the protocol type for this route, TCP, UDP, or TLS.

Priority

This parameter specifies the route priority level. Lower values indicate higher priority.

Value range: 1—65535

Weight

This parameter specifies the route weight. Use this parameter only if two or more routes have the same priority. Higher values indicate which route has the higher priority.

Value range: 1—65535

Allow Less-Specific Route

This parameter specifies that the route can be less specific.

In Service

This parameter specifies whether this route has been taken out of service.

Note This parameter allows the administrator to effectively take a route out of service (versus removing it completely and re-adding it).

## Deleting a Static Route

This section describes how to delete a static route.

Step 1 Find the static route by using the procedure in the "Finding Static Routes" section .

Step 2 From list of matching records, choose the static route that you want to delete.

Step 3 To delete the static route, click the Delete Selected Item icon that displays in the tool bar in the upper, left corner of the window (or click the Delete Selected button that displays at the bottom of the window).

If the static route is not in use, Cisco Unified Presence Server deletes it. If it is in use, a message displays.

Additional Information

See the "Related Topics" section .

## Related Topics

• Finding Static Routes

• Configuring Static Routes

• Deleting a Static Route

| Field | Description |
|---|---|
| Destination Pattern | This field specifies the pattern of the incoming number. You can use "." as a wildcard for a single character and "*" as wildcard as a wildcard for multiple characters. A dash or hyphen, "-", is also allowed anywhere in the pattern Wildcard Usage For phones • A dot can exist anywhere in the pattern. • An asterisk can only exist at the end. For IP addresses and host names • An asterisk can be used as part of the a host name. • The dot acts as a literal value in a host name. An escaped asterisk sequence, \*, matches a literal * and can exist anywhere. |
| Description | This parameter specifies the description of a particular static route. |
| Next Hop | This parameter specifies the domain name or IP address of the destination (next hop) and can be specified as either a fully qualified domain name (FQDN) or dotted IP address. |
| Next Hop Port | This parameter specifies the port number of the destination (next hop). Default: 5060 |
| Route Type | This parameter specifies the route type, User or Domain. |
| Protocol Type | This parameter specifies the protocol type for this route, TCP, UDP, or TLS. |
| Priority | This parameter specifies the route priority level. Lower values indicate higher priority. Value range: 1—65535 |
| Weight | This parameter specifies the route weight. Use this parameter only if two or more routes have the same priority. Higher values indicate which route has the higher priority. Value range: 1—65535 |
| Allow Less-Specific Route | This parameter specifies that the route can be less specific. |
| In Service | This parameter specifies whether this route has been taken out of service. Note This parameter allows the administrator to effectively take a route out of service (versus removing it completely and re-adding it). |