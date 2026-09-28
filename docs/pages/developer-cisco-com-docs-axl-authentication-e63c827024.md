---
doc_id: developer-cisco-com-docs-axl-authentication-e63c827024
source_url: https://developer.cisco.com/docs/axl/authentication/
retrieved_at: 2026-09-27T15:39:27.068543+00:00
---

# Authentication

## Overview

AXL limits access to its services through HTTP 1.0 Basic Access Authentication. It is a transaction scheme described in RFC 2617 . The advantage of HTTP Basic Access Authentication is that it's simple to implement. It uses only standard HTTP headers and, when using a Web browser, the browser implements and manages the login dialog.

## Using Basic Authentication

HTTP Basic Access Authentication requires authorization credentials in the form of a user name and password before granting access to a specific URL. The client application can obtain the user name and password through a challenge dialog, or it can use previously stored values. The user name and password are passed as Base64 encoded text in the header of a subsequent HTTP transaction.

All AXL API requests require authentication for access. Use an end user account created by the CUCM administrator to make API calls that require authentication.

Note: As of CUCM v11.5(1), AXL supports both Read and Read/Write access roles for AXL API users.

Service Activation and User/Group management is handled in Communications Manager Serviceability. Make sure the AXL services status is started:

Create a dedicated user for AXL Access:

- It is recommended that a User and Group for your application be created, rather than using the admin user.

- Create special application user for AXL access

- Create User Group for AXL access

- Put AXL user in this user group

Adding Read-Only or Read/Write access roles to the User Group:

- To enable full Read/Write access for the User Group, select the 'Standard AXL API Access' role

- To enable Read-Only access select the ‘Standard AXL API Users’ and ‘Standard AXL Read Only API Access’ roles

- All AXL requests must be authorized

- AXL requests are authorized using HTTPS basic authorization

- Authorization header with : in BASE64 coding

- Authorization: Basic YXhsVXNlcjpjaXNjbw==

- BASE64 coding can EASILY be decoded

- Authorization secure only because HTTPS is used

- AXL API access is a dedicated role in Communications Manager

- User for AXL API access can/should be limited to AXL API access only

Note: AXL requests by a read-only user that fail when attempting a write/update operation will return a standard HTTP 401 'Unauthorized' message.

## Security

Cisco requires that all AXL transactions be conducted over a secure session, such as HTTPS. Any non-HTTPS requests will be redirected to the HTTPS port.

Depending on the connection technology used, you may need to manually install the Unified Communication Manager's self-signed certificate into a local trust store for your application.

# Authentication Best Practices

A client application that intends to perform multiple requests should maintain an AXL session by supplying a session cookie when it makes subsequent requests.  This will ensure quicker responses and less overhead on CUCM and its authentication mechanisms (avoiding throttling and HTTP 503 "Service Unavailable" responses.)

Client requests which are authenticated via Basic Auth are given a cookie named 'JSESSIONIDSSO' in the response.  This cookie can be provided in subsequent requests (instead of of the Basic Auth 'Authorization' header) to re-use the AXL authentication session.

http

```
Cookie : JSESSIONIDSSO=2723FD93559E7FA7E17F0E7958D13; Path=/; Secure; HttpOnly
```

A developer should code their client to properly handle this cookie. In most HTTP libraries, this is simple and usually involves only a few lines of code.

Next